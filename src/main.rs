mod p1;
mod p2;
mod p3;
mod p3_2;
mod p4;
mod p5;
mod p6;
mod p8;
mod p9_1;
mod p10;


fn main() {
    println!("-----------Day 1-----------");
    p1::solve_p1();
    println!("-----------Day 2-----------");
    p2::solve_p2();
    println!("-----------Day 3-----------");
    p3::solve_p3();
    p3_2::solve_p3();
    println!("-----------Day 4-----------");
    p4::solve_p4();
    println!("-----------Day 5-----------");
    p5::solve_p5(1);
    p5::solve_p5(2);
    println!("-----------Day 6-----------");
    p6::solve_p6(1);
    p6::solve_p6(2);
    println!("-----------Day 8-----------");
    p8::solve_p8();
    println!("-----------Day 9-----------");
    p9_1::solve_p9();
    println!("-----------Day 10-----------");
    p10::solve_p10();
}
