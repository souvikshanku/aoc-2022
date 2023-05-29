use std::collections::HashMap;
use std::fs;


pub fn solve_p2() {

    let file_path = "./inputs/p2.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let contents_split: Vec<_> = contents.split("\n").collect();

    let score_dict = HashMap::from([
        // Draw
        ("A X", 1 + 3),
        ("B Y", 2 + 3),
        ("C Z", 3 + 3),
        // Loss
        ("A Z", 3 + 0),
        ("B X", 1 + 0),
        ("C Y", 2 + 0),
        // Win
        ("A Y", 2 + 6),
        ("B Z", 3 + 6),
        ("C X", 1 + 6)
    ]);

    let mut sum: i32 = 0;

    for pair in contents_split.clone(){
        sum += score_dict[pair];
    }

    println!("Part 1 Score: {}", sum);

    let score_dict2 = HashMap::from([
        // Lose
        ("A X", 3 + 0),
        ("B X", 1 + 0),
        ("C X", 2 + 0),
        // Draw
        ("A Y", 1 + 3),
        ("B Y", 2 + 3),
        ("C Y", 3 + 3),
        // Win
        ("A Z", 2 + 6),
        ("B Z", 3 + 6),
        ("C Z", 1 + 6)
    ]);

    let mut sum2: i32 = 0;

    for pair in contents_split{
        sum2 += score_dict2[pair];
    }

    println!("Part 2 Score: {}", sum2);
}
