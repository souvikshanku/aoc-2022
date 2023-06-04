use std::fs;
use std::collections::HashSet;


pub fn solve_p6(part: usize) {
    let file_path = "./inputs/p6.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

        let str_vec: Vec<_> =  contents.chars().collect();

    let mut start = 0;
    let mut end = 4;

    if part == 2 {
        end = 14;
    }

    while end <= str_vec.len() {
        if !check_len_le_4(str_vec[start..end].to_vec(), part) {
            break;
        }

        start += 1;
        end += 1;
    }
    
    println!("{}", end);

}


fn check_len_le_4(subarray:  Vec<char>, part: usize) -> bool {
    let mut unique_chars = HashSet::new();
    for letter in subarray {
        unique_chars.insert(letter);
    }

    let mut limit = 4;
    if part == 2 {
        limit = 14;
    }

    if unique_chars.len() < limit {
        return true
    } else {return false}

}
