use std::fs;
use std::collections::HashSet;


pub fn solve_p9() {
    let file_path = "./inputs/p9.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let movements: Vec<_> = contents.split("\n").collect();


    let mut vis_pos = HashSet::new();
    let mut head_pos = (0, 0);
    let mut tail_pos = (0, 0);

    vis_pos.insert(tail_pos);

    for movement in &movements {
        let dir: Vec<_> = movement.split(" ").collect();

        if dir[0] == "L" {
            let num_move = dir[1].to_string().parse::<isize>().unwrap();
            head_pos = (head_pos.0 - num_move as isize, head_pos.1);
            
            if abs(head_pos.1 - tail_pos.1) == 1 {
                let diff = abs(tail_pos.0 - head_pos.0);
                if diff <= 1 {
                    continue;
                } else {
                    for _ in 0..(diff-1) {
                        tail_pos = (tail_pos.0 - 1, head_pos.1);
                        vis_pos.insert(tail_pos);
                    }
                }
            } else {
                let mut diff = abs(tail_pos.0 - head_pos.0);
                while diff > 1 {
                    tail_pos = (tail_pos.0 - 1, head_pos.1);
                    vis_pos.insert(tail_pos);
                    diff -= 1;
                }
            }

        } else if dir[0] == "R" {
            let num_move = dir[1].to_string().parse::<isize>().unwrap();
            head_pos = (head_pos.0 + num_move as isize, head_pos.1);
            
            if abs(head_pos.1 - tail_pos.1) == 1 {
                let diff = abs(tail_pos.0 - head_pos.0);
                if diff <= 1 {
                    continue;
                } else {
                    for _ in 0..(diff-1) {
                        tail_pos = (tail_pos.0 + 1, head_pos.1);
                        vis_pos.insert(tail_pos);
                    }
                }
            } else {
                let mut diff = abs(tail_pos.0 - head_pos.0);
                while diff > 1 {
                    tail_pos = (tail_pos.0 + 1, head_pos.1);
                    vis_pos.insert(tail_pos);
                    diff -= 1;
                }
            }
        } else if dir[0] == "U" {
            let num_move = dir[1].to_string().parse::<isize>().unwrap();
            head_pos = (head_pos.0, head_pos.1 + num_move as isize);
            
            if abs(head_pos.0 - tail_pos.0) == 1 {
                let diff = abs(tail_pos.1 - head_pos.1);
                if diff <= 1 {
                    continue;
                } else {
                    for _ in 0..(diff-1) {
                        tail_pos = (head_pos.0, tail_pos.1 + 1);
                        vis_pos.insert(tail_pos);
                    }
                }
            } else {
                let mut diff = abs(tail_pos.1 - head_pos.1);
                while diff > 1 {
                    tail_pos = (tail_pos.0, tail_pos.1 + 1);
                    vis_pos.insert(tail_pos);
                    diff -= 1;
                }
            }
        } else {
            let num_move = dir[1].to_string().parse::<isize>().unwrap();
            head_pos = (head_pos.0, head_pos.1 - num_move as isize);
            
            if abs(head_pos.0 - tail_pos.0) == 1 {
                let diff = abs(tail_pos.1 - head_pos.1);
                if diff <= 1 {
                    continue;
                } else {
                    for _ in 0..(diff-1) {
                        tail_pos = (head_pos.0, tail_pos.1 - 1);
                        vis_pos.insert(tail_pos);
                    }
                }
            } else {
                let mut diff = abs(tail_pos.1 - head_pos.1);
                while diff > 1 {
                    tail_pos = (tail_pos.0, tail_pos.1 - 1);
                    vis_pos.insert(tail_pos);
                    diff -= 1;
                }
            }
        }
    }

    println!("{:?}", vis_pos.len());
}


fn abs(x: isize) -> isize {
    if x < 0 {
        return - x;
    } else {
        return x;
    }
}
