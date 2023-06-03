use std::fs;


pub fn solve_p5() {
    let file_path = "./inputs/p5.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let assignments: Vec<_> = contents.split("\n\n").collect();
    let arrays: Vec<_> = assignments[0].split("\n").collect();
    let _commands: Vec<_> = assignments[1].split("\n").collect();

    let len_array: Vec<_> = arrays[arrays.len() -1].trim().split(" ").collect();
    let array_count = len_array[len_array.len() - 1].parse::<i32>().unwrap();

    let mut all_arrays = vec![vec![String::new()]; array_count.try_into().unwrap()];

    for i in 0..array_count as usize {
        let crates_and_other_chars: Vec<_> = arrays[i].chars().collect();
        let mut crates = vec!['_'; array_count.try_into().unwrap()];

        let mut idx = 1;
        for j in 0..array_count as usize {
            crates[j] = crates_and_other_chars[idx];
            idx += 4
        }
        // println!("{:?}", crates);

        let mut crate_idx: usize = 0;
        for letter in &crates {
            if letter.to_string() != " " {
                if all_arrays[crate_idx][0] == "" {
                    all_arrays[crate_idx][0] = letter.to_string();
                } else {
                    all_arrays[crate_idx].push(letter.to_string())
                }
            } else {
                crate_idx += 1;
                continue;
            }

            crate_idx += 1;
        }
    }


    for i in 0..array_count as usize {
        let mut rev_array = all_arrays[i].clone();
        rev_array.reverse();
        all_arrays[i] = rev_array;
    }

    println!("{:?}", all_arrays);
    println!("---------------------------");

    for command in _commands {
        let indicator: Vec<_> = command.split(" ").collect();

        let a_ind = indicator[3].parse::<usize>().unwrap();
        let b_ind = indicator[5].parse::<usize>().unwrap();
        let m = indicator[1].parse::<usize>().unwrap();

        (all_arrays[a_ind -1], all_arrays[b_ind -1]) = move_by_command(
            all_arrays[a_ind -1].clone(),
            all_arrays[b_ind -1].clone(), 
            m
        );
    }

    println!("{:?}", all_arrays);
    for array in &all_arrays {
        print!("{}", array[array.len() - 1]);
    }
    println!("\n");

   
}

fn move_by_command(mut a: Vec<String>, mut b: Vec<String>, m: usize) -> (Vec<String>, Vec<String>){
    for _i in 0..m {
        let moved_letter = a.pop().unwrap();
        b.push(moved_letter);
    }
    (a, b)
}