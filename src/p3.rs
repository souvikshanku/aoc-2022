use std::fs;


pub fn solve_p3() {
    let file_path = "./inputs/p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let rucksacks: Vec<_> = contents.split("\n").collect();

    let mut sum: usize = 0;
    for rucksack in &rucksacks{
        sum += check_common_item(rucksack);
    }

    println!("{}", sum);
}


fn get_value_from_alpha(alpha: &str) -> usize {
    let small: Vec<_> = "abcdefghijklmnopqrstuvwxyz".split("").collect();
    let caps: Vec<_> = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").collect();

    for idx in 0..small.len() {
        if alpha == small[idx] {
            return idx
        }
    }

    for idx in 0..caps.len() {
        if alpha == caps[idx] {
            return idx + 26
        }
    }

    return 0

}

fn check_common_item(rucksack: &str) -> usize {
    let rucksack: Vec<char> = rucksack.chars().collect();
    let length = rucksack.len();
    let half_length = length/ 2;

    let mut first_half: Vec<_> = vec!['-'; half_length];
    let mut second_half: Vec<_> = vec!['-'; half_length];

    for i in 0..half_length {
        first_half[i] = rucksack[i];
    }

    for i in 0..half_length {
        second_half[i] = rucksack[half_length + i];
    }
    
    let mut result: usize = 0;

    for i in 0..half_length {
        if second_half.contains(&first_half[i]) {
            result = get_value_from_alpha(&first_half[i].to_string());
            break;
        }
    }

    return result;
}
