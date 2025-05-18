
mod particles;
mod PSO;

mod benchmark_functions;

fn main(){

    /*
        griewank{dim: 5, n: 50_000, c: 1.49445f32, w: 0.7, k: true}
        griewank{dim: 5, n: 50_000, c: 1.49445f32, w: 0.7, k: false}

        griewank{dim: 10, n: 500_000, c: 1.49445f32, w: 0.7, k: true}
        griewank{dim: 10, n: 500_000, c: 1.49445f32, w: 0.7, k: false}

        ackley{dim: 5, n: 50_000, c: 1.49445f32, w: 0.7, k: true}
        ackley{dim: 5, n: 50_000, c: 1.49445f32, w: 0.7, k: false}

        ackley{dim: 10, n: 500_000, c: 1.49445f32, w: 0.7, k: true}
        ackley{dim: 10, n: 500_000, c: 1.49445f32, w: 0.7, k: false}
    
     */
 
    match  PSO::PSO(500_000, 30, 10, benchmark_functions::griewank, (-32f32, 32f32), 1.49445f32, 0.7f32, false){
        Ok(r) => {
            let (best_solution, res_func, X) = r;
            println!("Best Solution: {:?}, Y: {:?}", best_solution, X);
        },
        Err(e) => {println!("Error: {e}");}
    }


}


