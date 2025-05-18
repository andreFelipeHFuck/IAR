use std::fmt;

use crate::benchmark_functions;


pub fn create_random_matrix(dim: usize, num: usize, range: (f32, f32)) -> Result<Vec<Vec<f32>>, benchmark_functions::FuncError
> {
    let mut res_vec: Vec<Vec<f32>> = vec![vec![0.0;dim];num];

    if range.1 > range.0 {
        for i in 0..num{
            for j in 0..dim{
                res_vec[i][j] = rand::random_range(range.0..=range.1/2f32);
            }
        }

        Ok(res_vec)
    }else{
        Err(benchmark_functions::FuncError::OutOfDomain)
    }
}


pub fn smallest_solution(matrix: &Vec<Vec<f32>>, range: f32) -> Vec<f32> {
    let mut smaller: bool = false;
    let mut res = vec![0.0; matrix[0].len()];

    for i in 0..res.len(){
        res[i] = range;
    }

    for i in 0..matrix.len() {
        for j in 0..res.len() {
            if matrix[i][j] <= res[j] {
                smaller = true;
            }else{
                smaller = false;
                break;
            }
        }

        if smaller {
            for j in 0..res.len() {
                res[j] = matrix[i][j];
            }
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

    w: f32, // peso de inércia
    k: f32 // fator de constrição
}


impl fmt::Display for Particles {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Num: {}\nDimensions: {}\nBest Solution: {:?}\nX: {:?}\nV: {:?}\nY: {:?}\nw: {}\nk: {}\n", self.num, self.dimensions, self.best_solution, self.X, self.V, self.Y, self.w, self.k)
    }
}

impl Particles {
    pub fn new(n: u32, dim: u32, f:fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>, x: (f32, f32), w: f32, c: f32, k: bool) -> Result<Self, benchmark_functions::FuncError> {
        let res_k;
        let c = 2.05f32;
        if !k {
            res_k = 0.0;
        }else{
            let fi = 2f32 * c;
            res_k = 2f32 / (2f32 - fi - (fi.powf(2f32) - 4f32 * fi).sqrt()).abs();
        }

        let X = create_random_matrix(dim as usize, n as usize, (x.0, x.1))?;

        Ok(Particles {
            num: n,
            dimensions: dim,
            func: f,

            best_solution: smallest_solution(&X,  x.1),

            X: X.clone(),
            X_min: x.0,
            X_max: x. 1,

            V: create_random_matrix(dim as usize, n as usize, (x.0, x.1))?,
            V_min: x.0,
            V_max: x.1, 

            Y: X.clone(),
            c_1: c,
            c_2: c,

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

  pub fn get_Y(&mut self) -> Vec<Vec<f32>> {
    self.Y.clone()
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
                if self.k > 0.0 {
                    self.V[i][j as usize] = self.k * (self.V[i][j as usize] + self.c_1 * rand::random_range(0.0..=1.0) * (self.Y[i][j as usize] - self.X[i][j as usize]) + self.c_2 * rand::random_range(0.0..=1.0) * (self.best_solution[j as usize] -  self.X[i][j as usize]));                    
                }else {
                    self.V[i][j as usize] = self.w * self.V[i][j as usize] + self.c_1 * rand::random_range(0.0..=1.0) * (self.Y[i][j as usize] - self.X[i][j as usize]) + self.c_2 * rand::random_range(0.0..=1.0) * (self.best_solution[j as usize] -  self.X[i][j as usize]);
                }
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

