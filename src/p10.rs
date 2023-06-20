use std::fs;


pub fn solve_p10() {
    let file_path = "./inputs/p10.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let instrs: Vec<_> = contents.split("\n").collect();
    // println!("{:?}", instrs);

    let mut cycle = 0;
    let mut value = 1;

    let mut value_array = vec![0, 0, 0, 0, 0, 0];
    let cycle_array = vec![20, 60, 100, 140, 180, 220];

    let mut compare_idx = 0;

    for instr in instrs {
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
        // println!("{}", idx)
        result += value_array[idx] * cycle_array[idx]
    }
    println!("{:?}", result)
}
