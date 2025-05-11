
mod particles;
mod PSO;

mod benchmark_functions;

fn main(){
 
    match  PSO::PSO(10_000, 10, 2, benchmark_functions::griewank, (-600f32, 600f32), 1f32, false){
        Ok(r) => {
            let (best_solution, res_func, X) = r;
            println!("Best Solution: {:?},  X: {:?}", best_solution,  X);
        },
        Err(e) => {println!("Error: {e}");}
    }


}


