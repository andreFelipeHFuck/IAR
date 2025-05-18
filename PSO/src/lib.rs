use pyo3::prelude::*;

use pyo3::wrap_pyfunction;

mod particles;
mod benchmark_functions;

fn particleSwarmOptimization(num_iteration: u32, n: u32, dim: u32, f:fn(u32, &Vec<f32>) -> Result<f32, benchmark_functions::FuncError>, x: (f32, f32), c: f32, w: f32, k: bool) -> Result<(Vec<f32>, f32, Vec<f32>, Vec<Vec<f32>>), benchmark_functions::FuncError> {
   let mut res_func: Vec<f32> = vec![];

    let mut S= particles::Particles::new(n, dim, f, x, w, c, k)?;

        for _ in 0..num_iteration{
            let best_solution: f32 = S.calcule_func_best_solution()?;
            for i in 0..S.get_n(){

                if S.calcule_func_x_i(i as usize)? < S.calcule_func_y_i(i as usize)? {
                    S.update_Y_i(i as usize);
                }
    
                if S.calcule_func_y_i(i as usize)? < best_solution {
                    S.update_best_solution(i as usize);
                   
                }

            }
            res_func.push(S.calcule_func_best_solution()?);
    
            S.update_X();
        }

        return Ok((S.get_best_solution(), S.calcule_func_best_solution()?, res_func, S.get_Y()));
    
}

#[pyclass]
#[derive(Debug, Clone)]
enum Func {
    Ackley,
    Griewank
}

use Func::{*};


#[pymodule(name = "PSO")]
fn my_extension(m: &Bound<'_, PyModule>) -> PyResult<()> {

    fn map_error(_py: Python, error: benchmark_functions::FuncError) -> PyErr {
        match error {
            benchmark_functions::FuncError::OutOfDomain => PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "Valor fora do domínio da função, a função temo domínio de -32 a 32",
            )
        }
    }

    #[pyfunction]
    fn ackley(py: Python, dim: u32, values: Vec<f32>) -> PyResult<f32>{
        match benchmark_functions::ackley(dim, &values) {
            Ok(v) => {Ok(v)},
            Err(e) => {Err(map_error(py, e))}
        }
    }

    #[pyfunction]
    fn griewank(py: Python, dim: u32, values: Vec<f32>) -> PyResult<f32>{
        match benchmark_functions::griewank(dim, &values)  {
            Ok(v) => {Ok(v)},
            Err(e) => {Err(map_error(py, e))}
        }
    }

    #[pyfunction]
    fn pso(py: Python, num_iteration: u32, n: u32, dim: u32, f: Func, c:f32, w: f32, k: bool) -> PyResult<(Vec<f32>, f32, Vec<f32>, Vec<Vec<f32>>)> {
        match f {
            Ackley => {
                match particleSwarmOptimization(num_iteration, n, dim, benchmark_functions::ackley, (-32f32, 32f32), c, w, k) {
                    Ok(res) =>{Ok(res)},
                    Err(e) => {Err(map_error(py, e))}
                }
            }
            Griewank => {
                match particleSwarmOptimization(num_iteration, n, dim, benchmark_functions::griewank, (-600f32, 600f32), c, w, k) {
                    Ok(res) =>{Ok(res)},
                    Err(e) => {Err(map_error(py, e))}
                }
            }
        }
    }
   
    m.add_function(wrap_pyfunction!(ackley, m)?);
    m.add_function(wrap_pyfunction!(griewank, m)?);
    m.add_function(wrap_pyfunction!(pso, m)?);
    m.add_class::<Func>()?;

    Ok(())

}