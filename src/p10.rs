use std::fs;


pub fn solve_p10() {
    let file_path = "./inputs/p10.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let instrs: Vec<_> = contents.split("\n").collect();

    let mut cycle = 0;
    let mut value = 1;

    let mut value_array = vec![0, 0, 0, 0, 0, 0];
    let cycle_array = vec![20, 60, 100, 140, 180, 220];

    let mut compare_idx = 0;

    for instr in &instrs {
        let task: Vec<_> = instr.split(" ").collect();

        // println!("{:?}", task);
        if task[0] == "noop" {
            cycle += 1;
            if cycle >= cycle_array[compare_idx] {
                // println!("final value: {}", value);
                value_array[compare_idx] = value;
                compare_idx += 1;
                // break;
            }
        }
        else {
            cycle += 2;
            if cycle >= cycle_array[compare_idx] {
                // println!("final value: {}", value);
                value_array[compare_idx] = value;
                compare_idx += 1;
                // break;
            }
            value += task[1].to_string().parse::<isize>().unwrap();
        }

        if compare_idx == 6 {
            break;
        }
        
    }

    let mut result = 0;

    for idx in 0..6 {
        result += value_array[idx] * cycle_array[idx]
    }
    println!("{:?}", result);


    let mut cycle = 0;
    let mut value = 1;
    let mut all_values = vec![0; 240];
    let mut pixel_array: Vec<_> = vec!["  "; 240];
    let mut idx = 0;

    for instr in instrs {
        let task: Vec<_> = instr.split(" ").collect();

        if task[0] == "noop" {
            all_values[idx] = value;
            cycle += 1;
            idx += 1;
        }
        else {
            for i in (idx)..(idx+2) {
                all_values[i] = value;
            }
            cycle += 2;
            value += task[1].to_string().parse::<isize>().unwrap();
            all_values[idx+2] = value;
            idx += 2;
        }
    }
    for c in 0..240 {
        let sprite_pos = c as isize % 40;
        let x = all_values[c];
        if x == sprite_pos || x == (sprite_pos - 1) || x == (sprite_pos + 1) {
            pixel_array[c] = "##";
        }
    }

    let mut idx = 0;
    for i in 0..6 {
        println!("{:?}", &pixel_array[idx..(idx+40)]);
        idx += 40;
    }
}
