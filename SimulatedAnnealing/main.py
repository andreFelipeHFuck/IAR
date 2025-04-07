

def main(path: str) -> None:
    n_lit, c_list = readCnfFile(path=path)
    
    clauses = Clauses(n_lit, c_list)
    
    SA_max = 1
    
    N = 1_000
    T0_1 = generate_T0_average(clauses, n_lit, N) 
    
    TN = 0.000_1
        
    l = Literals(n_lit)
    l.generate_random_literals()
    clauses.calcule_all_clauses_falses(l)
    
    print(f"T0_1_average: {T0_1}\n")

    print(l)
    
    s_1, list_interation, list_values, list_temperature = simulatedAnnealing(clauses, cooling.cooling_schedule_1, SA_max, T0_1, TN, N, l)
            
    print(s_1)
    
    clauses.calcule_all_clauses_falses(s_1)
    
    graphics.create_plot(list_interation, list_values, list_temperature, 1)
        
 
if __name__ == '__main__':
    main("uf20-01.cnf")
    

