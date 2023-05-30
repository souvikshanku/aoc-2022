use std::fs;


pub fn solve_p4() {
    let file_path = "./inputs/p4.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let assignments: Vec<_> = contents.split("\n").collect();

    let mut count1: usize = 0;
    let mut count2: usize = 0;

    for assignment in assignments {
        let a_vec: Vec<_> = assignment.split(",").collect();

        let a = a_vec[0];
        let b = a_vec[1];

        let a: Vec<_> = a.split("-").collect();
        let b: Vec<_> = b.split("-").collect();

        let a1 = a[0].parse::<i32>().unwrap();
        let a2 = a[1].parse::<i32>().unwrap();
        let b1 = b[0].parse::<i32>().unwrap();
        let b2 = b[1].parse::<i32>().unwrap();

        if a1 <= b1 && a2 >= b2 {
            count1 += 1;
        } else if a1 >= b1 && a2 <= b2 {
            count1 += 1;
        }

        if a1 <= b1 && a2 >= b1 {
            count2 += 1;
        } else if b1 <= a1 && b2 >= a1 {
            count2 += 1;
        }
    }

    println!("{:?}", count1);
    println!("{:?}", count2);
}