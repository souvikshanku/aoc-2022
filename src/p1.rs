use std::fs;

pub fn solve_p1() {
    let file_path = "./inputs/p1.txt";

    let contents =
        fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let contents_split: Vec<_> = contents.split("\n\n").collect();

    let mut max_sum1: i32 = 0;
    let mut max_sum2: i32 = 0;
    let mut max_sum3: i32 = 0;
    let mut current_sum: i32 = 0;

    for part in contents_split {
        let small_part: Vec<_> = part.split("\n").collect();

        for num_in_str in small_part {
            let num: i32 = num_in_str.trim().parse().unwrap();
            current_sum += num;
        }

        if current_sum >= max_sum1 {
            max_sum3 = max_sum2;
            max_sum2 = max_sum1;
            max_sum1 = current_sum;
        } else if current_sum >= max_sum2 {
            max_sum3 = max_sum2;
            max_sum2 = current_sum;
        } else if current_sum >= max_sum3 {
            max_sum3 = current_sum;
        }

        current_sum = 0;
    }

    println!("{0}, {1}, {2}", max_sum1, max_sum2, max_sum3);
    println!("{0}", max_sum1 + max_sum2 + max_sum3);
}
