use core::fmt;

#[derive(Debug)]
pub enum FuncError {
    OutOfDomain
}

impl fmt::Display for FuncError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match  self {
            FuncError::OutOfDomain => write!(f, "Valor fora do domínio da função, a função temo domínio de -32 a 32")
        }
    }
}

impl std::error::Error for FuncError {}

pub fn griewank(dim: u32, values: &Vec<f32>) -> Result<f32, FuncError>{
    let mut top1: f32 = 0.0;
    let mut top2: f32 = 1.0;

    for i in 1..=dim {
        top1 += values[(i - 1) as usize].powf(2f32);
        top2 *=  ((values[(i - 1) as usize] / (i as f32).sqrt())).cos();
    }

    Ok((1f32/4000f32) * top1 - top2 + 1f32)
}

pub fn ackley(dim: u32, values: &Vec<f32>) -> Result<f32, FuncError> {
    let a = 20f32;
    let b = 0.2f32;
    let c = 2.0 * std::f32::consts::PI;

    let div_dim = 1f32 / dim as f32;

    let mut aux: f32 = 0.0;
    let mut aux1: f32 = 0.0;

    for i in 1..=dim{
        if values[(i - 1) as usize] >=-32f32 || values[(i - 1) as usize] <= 32f32 {
            aux += values[(i - 1) as usize].powf(2f32);
            aux1 += c*values[(i - 1) as usize].cos();

        }else{
            return Err(FuncError::OutOfDomain);
        }

    }

    Ok(a * (-b * (div_dim * aux).sqrt()).exp() - (div_dim * aux1).exp() + a + 1f32.exp())
}

