# Initial Y value
Y0 = 0

np.random.seed(0)

# Number of years simulated and number of simulations
n_years = 10
n_simulations = 100000

t = np.array(range(0,n_years+1))

Z_mont1 = norm.rvs(size = [n_simulations,n_years])
Z_mont2 = norm.rvs(size = [n_simulations,n_years])
r_simtemp = np.zeros([n_simulations, n_years+1])
Y_simtemp = np.zeros([n_simulations, n_years+1])

#Sets the first column (the initial value of each simulation) to r(0) and Y0
r_simtemp[:,0] = r0 
Y_simtemp[:,0] = Y0

correlations = rY_rho(t[0:-1],t[1:])
Z_mont2 = correlations*Z_mont1 + np.sqrt(1-correlations**2)*Z_mont2 #Creating correlated standard normals

for i in range(n_years):
    r_simtemp[:,i+1] = vasi_mean(r_simtemp[:,i],t[i],t[i+1]) + np.sqrt(vasi_var(t[i],t[i+1]))*Z_mont1[:,i]
    Y_simtemp[:,i+1] = Y_mean(Y_simtemp[:,i],r_simtemp[:,i],t[i],t[i+1]) + np.sqrt(Y_var(t[i],t[i+1]))*Z_mont2[:,i]
    
ZCB_prices = np.mean(np.exp(-Y_simtemp),axis = 0)