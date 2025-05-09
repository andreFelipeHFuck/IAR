use crate::benchmark_functions;
use crate::particles;

pub fn PSO(num_iteration: u32, n: u32, dim: u32, f:fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>, x: (f32, f32), w: f32, k: bool) -> Result<(Vec<f32>, Vec<Vec<f32>>), benchmark_functions::FuncError> {
    let mut S= particles::Particles::new(n, dim, f, x, w, k)?;
    println!("{}", S);

        for n_i in 0..num_iteration{
            for i in 0..S.get_n(){
                let f_y_i = S.calcule_func_y_i(i as usize)?;
    
                if S.calcule_func_x_i(i as usize)? < f_y_i {
                    S.update_Y_i(i as usize);
                }
    
                if f_y_i < S.calcule_func_best_solution()?  {
                    S.update_best_solution(i as usize);
                }
            }
    
            S.update_X();
        }

        return Ok((S.get_best_solution(), S.get_X()));
    
}