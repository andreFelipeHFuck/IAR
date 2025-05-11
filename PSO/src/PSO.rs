use crate::benchmark_functions;

use crate::particles;


pub fn PSO(num_iteration: u32, n: u32, dim: u32, f:fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>, x: (f32, f32), w: f32, k: bool) -> Result<(Vec<f32>, Vec<f32>, Vec<Vec<f32>>), benchmark_functions::FuncError> {
    let mut res_func: Vec<f32> = vec![];

    let mut S= particles::Particles::new(n, dim, f, x, w, k)?;
    println!("{}", S);

        for n_i in 0..num_iteration{
            for i in 0..S.get_n(){
                let best_solution: f32 = S.calcule_func_best_solution()?;

                if S.calcule_func_x_i(i as usize)? < S.calcule_func_y_i(i as usize)? {
                    S.update_Y_i(i as usize);
                }
    
                if S.calcule_func_y_i(i as usize)? < best_solution {
                    S.update_best_solution(i as usize);
                }

                res_func.push(best_solution);
            }
    
            S.update_X();
        }

        return Ok((S.get_best_solution(), res_func, S.get_X()));
    
}