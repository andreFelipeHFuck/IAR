use std::vec;

use rand::prelude::*;

use crate::benchmark_functions;


pub fn create_random_matrix(dim: usize, num: usize, range: (f32, f32)) -> Result<Vec<Vec<f32>>, benchmark_functions::FuncError
> {
    let mut res_vec: Vec<Vec<f32>> = vec![vec![0.0;dim];num];

    if range.1 > range.0 {
        for i in 0..num{
            for j in 0..dim{
                res_vec[i][j] = rand::random_range(range.0..=range.1);
            }
        }

        Ok(res_vec)
    }else{
        Err(benchmark_functions::FuncError::OutOfDomain)
    }
}

pub fn create_random_vec(num: usize, range: (f32, f32)) -> Result<Vec<f32>, benchmark_functions::FuncError> {
    let mut res_vec: Vec<f32> = vec![0.0;num];

    if range.1 > range.0 {
        for i in 0..res_vec.len(){
            res_vec[i] = rand::random_range(range.0..=range.1);
        }
        
        Ok(res_vec)
    }else{
        Err(benchmark_functions::FuncError::OutOfDomain)
    }
}


pub fn smallest_solution(matrix: &Vec<Vec<f32>>, range: (f32, f32)) -> Vec<f32> {
    let mut res = vec![
        matrix[0][0],
        matrix[0][1],
    ];

    for i in 0..matrix.len() {
        if matrix[i][0] < res[0] && matrix[i][1] < res[1] {
            res[0] = matrix[i][0];
            res[1] = matrix[i][1];
        }
    }

    res
}