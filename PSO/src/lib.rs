use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod benchmark_functions;

#[pyfunction]
fn double(x: usize) -> usize {
    x * 2
}




#[pymodule(name = "PSO")]
fn my_extension(m: &Bound<'_, PyModule>) -> PyResult<()> {

    fn map_error(py: Python, error: benchmark_functions::FuncError) -> PyErr {
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

    m.add_function(wrap_pyfunction!(ackley, m)?);
    m.add_function(wrap_pyfunction!(griewank, m)?);

    Ok(())

}