use std::fmt;

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


pub fn smallest_solution(matrix: &Vec<Vec<f32>>) -> Vec<f32> {
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

#[derive(Debug)]
pub struct Particles {
    num: u32,
    dimensions: u32,
    func: fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>,

    best_solution: Vec<f32>, 

    X: Vec<Vec<f32>>, // Positions
    X_min: f32,
    X_max: f32,

    V: Vec<Vec<f32>>, // Displacement
    V_min: f32,
    V_max: f32,

    Y: Vec<Vec<f32>>,// Cognitive Component

    c_1: f32,
    c_2: f32,

    r_1: Vec<f32>,
    r_2: Vec<f32>,

    w: f32, // peso de inércia
    k: f32 // fator de constrição
}


impl fmt::Display for Particles {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Num: {}\nDimensions: {}\nBest Solution: {:?}\nX: {:?}\nV: {:?}\nY: {:?}\nw: {}\nk: {}\n", self.num, self.dimensions, self.best_solution, self.X, self.V, self.Y, self.w, self.k)
    }
}

impl Particles {
    pub fn new(n: u32, dim: u32, f:fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>, x: (f32, f32), w: f32, k: bool) -> Result<Self, benchmark_functions::FuncError> {
        let res_k;
        if !k {
            res_k = 1.0;
        }else{
            res_k = 2.0;
            // Calculo de contrição
        }

        let X = create_random_matrix(dim as usize, n as usize, (x.0, x.1))?;

        Ok(Particles {
            num: n,
            dimensions: dim,
            func: f,

            best_solution: smallest_solution(&X),

            X: X.clone(),
            X_min: x.0,
            X_max: x. 1,

            V: create_random_matrix(dim as usize, n as usize, (x.0, x.1))?,
            V_min: x.0,
            V_max: x.1, 

            Y: X.clone(),
            c_1: 2.05,
            c_2: 2.05,

            r_1: create_random_vec(n as usize, (0.0, 1.0))?,
            r_2: create_random_vec(n as usize, (0.0, 1.0))?,

            w: w,
            k: res_k
        })
    }

  pub fn get_n(&mut self) -> u32{
    self.num
  }

  pub fn get_best_solution(&mut self) -> Vec<f32> {
    self.best_solution.clone()
  }

  pub fn get_X(&mut self) -> Vec<Vec<f32>> {
    self.X.clone()
  }

   pub fn calcule_func_x_i(&mut self, i: usize) -> Result<f32, benchmark_functions::FuncError> {
     (self.func)(self.dimensions, &self.X[i])
   }

   pub fn calcule_func_y_i(&mut self, i: usize) -> Result<f32, benchmark_functions::FuncError> {
      (self.func)(self.dimensions, &self.Y[i])
    } 

    pub fn calcule_func_best_solution(&mut self) -> Result<f32, benchmark_functions::FuncError> {
        (self.func)(self.dimensions, &self.best_solution)
    } 

   fn update_V_i(&mut self, i: usize) {
        for j in 0..self.dimensions{
            if self.X_min < self.V[i][j as usize] && self.V[i][j as usize] < self.X_max {
                self.V[i][j as usize] = self.V[i][j as usize] + self.c_1 * self.r_1[j as usize] * (self.Y[i][j as usize] - self.X[i][j as usize]) + self.c_2 * self.r_2[j as usize] * (self.best_solution[j as usize] -  self.X[i][j as usize]);
            }else{
                self.V[i][j as usize] = 0f32;
            }
        }
   }

   fn update_X_i(&mut self, i: usize) {
     self.update_V_i(i);

     for j in 0..self.dimensions{
        let rest = self.X[i][j as usize] + self.V[i][j as usize];

        if self.X_min <= rest && rest <= self.X_max {
            self.X[i][j as usize] = rest;
        }else if rest > self.X_max {
            self.X[i][j as usize] = self.X_max;
        }else{
            self.X[i][j as usize] = self.X_min;
        }
     }
   }

   pub fn update_X(&mut self) {
        for i in 0..self.num{
            self.update_X_i(i as usize);
        }
   }

   pub fn update_Y_i(&mut self, i: usize) {
        for j in 0..self.dimensions{
            self.Y[i][j as usize] = self.X[i][j as usize];
       }
   }

   pub fn update_best_solution(&mut self, i: usize) {
      for j in 0..self.dimensions{
        self.best_solution[j as usize] = self.Y[i][j as usize];
      }
   }


}

