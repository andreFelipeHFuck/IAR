use particles::Particles;

mod particles;
mod PSO;
mod utils;

mod benchmark_functions;

fn main(){
 
    match  PSO::PSO(1_000_000, 50, 2, benchmark_functions::ackley, (-32f32, 32f32), 1f32, false){
        Ok(r) => {
            let (best_solution, X) = r;
            println!("Best Solution: {:?}, X: {:?}", best_solution, X);
        },
        Err(e) => {println!("Error: {e}");}
    }


}


