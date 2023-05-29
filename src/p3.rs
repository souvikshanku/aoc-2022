// use std::collections::HashMap;
use std::fs;


pub fn solve_p3() {

    let file_path = "./inputs/p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let rucksacks: Vec<_> = contents.split("\n").collect();

    // println!("{:?}", rucksacks);
    for rucksack in &rucksacks[0..1]{
        check_common_item(rucksack);
    }
}


fn check_common_item(rucksack: &str) {

    let rucksack: Vec<char> = rucksack.chars().collect();
    let length = rucksack.len();
    let half_length = length/ 2;

    let mut first_half: Vec<_> = vec!['-'; half_length];
    let mut second_half: Vec<_> = vec!['-'; half_length];

    for i in 0..half_length {
        first_half[i] = rucksack[i];
    }

    // for j in half_length..length {
    //     second_half[j] = rucksack[j];
    // }

    println!("{:?}", first_half);
}
 