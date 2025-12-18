import math
import random
import time

def monte_carlo_european_school(S0, K, T, r, sigma, n_sims):
   
    drift = (r - 0.5 * sigma**2) * T
    vol_sqrt_T = sigma * math.sqrt(T)
    
    sum_payoffs = 0.0
    
 
    for i in range(n_sims):
        
        Z = random.gauss(0, 1)  # Loi Normale (moyenne 0, écart-type 1)
      
        ST = S0 * math.exp(drift + vol_sqrt_T * Z)
        
        payoff = max(ST - K, 0.0)
        
        sum_payoffs += payoff
        
    average_payoff = sum_payoffs / n_sims
    
    price = math.exp(-r * T) * average_payoff
    
    return price

# --- Paramètres ---
S0 = 100      
K = 100       
T = 1.0       
r = 0.05      
sigma = 0.2   
N = 1_000_000 # 1 million de simulations

# --- Exécution ---

start = time.time()

price = monte_carlo_european_school(S0, K, T, r, sigma, N)

end = time.time()

print(f"Prix estimé : {price:.4f}")
print(f"Temps de calcul : {end - start:.4f} secondes")