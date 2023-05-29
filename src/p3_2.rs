use std::fs;


pub fn solve_p3() {
    let file_path = "./inputs/p3.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let rucksacks: Vec<_> = contents.split("\n").collect();
    let count: usize = rucksacks.len() / 3;

    let mut sum: usize = 0;

    for i in 0..count {
        sum += check_common_item(rucksacks[3 * i], rucksacks[3 * i + 1], rucksacks[3 * i + 2]);
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


fn check_common_item(r1: &str, r2: &str, r3: &str) -> usize {

    let mut common_1_2: Vec<char> = Vec::new();
    let len1 = r1.len();

    for i in 0..len1 {
        let current_char = r1.chars().collect::<Vec<_>>()[i];
        if r2.contains(current_char) {
            common_1_2.push(current_char);
        }
    }


    let common_len = common_1_2.len();
    for i in 0..common_len {
        let current_char = common_1_2[i];
        if r3.contains(current_char) {
            return get_value_from_alpha(&current_char.to_string());
        }
    }

    return 0;
}

