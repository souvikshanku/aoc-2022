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
    let mut max_score = 0;

    for i in 1..(height - 1) {
        for j in 1..(width -1) {
            let (row_vis, row_score) = check_vis_in_row(&matrix, i, j);
            let (col_vis, col_score) = check_vis_in_col(&matrix, i, j);

            let score = row_score * col_score;
            if score > max_score {
                max_score = score;
            }

            if row_vis || col_vis {
                        vis_trees_count += 1; 
            }                
        }
    }

    println!("{:?}", vis_trees_count + 2 * width + 2 * (height - 2));
    println!("{:?}", max_score);
}

fn check_vis_in_row(matrix: &Vec<Vec<isize>>, row: usize, col: usize) -> (bool, usize) {
    let mut left_visibility = true;
    let mut right_visibility = true;

    let mut left_score = 0;
    let mut right_score = 0;

    for j in 0..col {
        if matrix[row][j] >= matrix[row][col] {
            left_visibility = false;
            break;
        }
    }

    for j in (0..col).rev() {
        left_score += 1;
        if matrix[row][j] >= matrix[row][col] {
            break;
        }
    }

    for j in (col+1)..matrix[0].len() {
        right_score += 1;
        if matrix[row][j] >= matrix[row][col] {
            right_visibility = false;
            break;
        }
    }

    return ((left_visibility || right_visibility), left_score * right_score)
}

fn check_vis_in_col(matrix: &Vec<Vec<isize>>, row: usize, col: usize) -> (bool, usize) {
    let mut up_visibility = true;
    let mut down_visibility = true;

    let mut up_score = 0;
    let mut down_score = 0;

    for i in 0..row {
        if matrix[i][col] >= matrix[row][col] {
            up_visibility = false;
            break;
        }
    }

    for i in (0..row).rev() {
        up_score += 1;
        if matrix[i][col] >= matrix[row][col] {
            break;
        }
    }

    for i in (row+1)..matrix.len() {
        down_score += 1;
        if matrix[i][col] >= matrix[row][col] {
            down_visibility = false;
            break;
        }
    }

    return  ((up_visibility || down_visibility), up_score * down_score)
}
