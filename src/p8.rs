#![allow(unused_assignments)]
use std::fs;


pub fn solve_p8() {
    let file_path = "./inputs/p8.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let trees: Vec<_> = contents.chars().collect();

    let temp: Vec<_> = contents.split("\n").collect();
    let height = temp.len();
    let width = temp[0].len();

    let mut matrix = vec![vec![0; width]; height];

    for i in 0..height {
        for j in 0..width {
            let new_line_count = (width * i + j) / width;
            let m_ij = trees[width * i + j + new_line_count] as usize;
            matrix[i][j] =  m_ij  as isize - 48;
        }
    }

    let mut vis_trees_count = 0;

    for i in 1..(height - 1) {
        for j in 1..(width -1) {
            if 
                check_vis_in_row(&matrix, i, j) 
                || check_vis_in_col(&matrix, i, j)
                    {
                        vis_trees_count += 1; 
                    }                
        }
    }

    println!("{:?}", vis_trees_count + 2 * width + 2 * (height - 2));
}


fn check_vis_in_row(matrix: &Vec<Vec<isize>>, row: usize, col: usize) -> bool {
    let mut left_visibility = true;
    let mut right_visibility = true;

    for j in 0..col {
        if matrix[row][j] >= matrix[row][col] {
            left_visibility = false;
            break;
        }
    }

    for j in (col+1)..matrix[0].len() {
        if matrix[row][j] >= matrix[row][col] {
            right_visibility = false;
            break;
        }
    }

    return left_visibility || right_visibility
}

fn check_vis_in_col(matrix: &Vec<Vec<isize>>, row: usize, col: usize) -> bool {
    let mut up_visibility = true;
    let mut down_visibility = true;

    for i in 0..row {
        if matrix[i][col] >= matrix[row][col] {
            up_visibility = false;
            break;
        }
    }

    for i in (row+1)..matrix.len() {
        if matrix[i][col] >= matrix[row][col] {
            down_visibility = false;
            break;
        }
    }

    return  up_visibility || down_visibility
}
