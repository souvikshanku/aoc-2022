use std::fs;


pub fn solve_p7() {
    let file_path = "./inputs/p7.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    
    println!("{:?}", contents);

}
