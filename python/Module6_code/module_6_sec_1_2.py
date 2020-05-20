# Simulating interest rate paths
# NB short rates are simulated on an annual basis
np.random.seed(0)

n_years = 10
n_simulations = 10

t = np.array(range(0,n_years+1))


Z = norm.rvs(size = [n_simulations,n_years])
r_sim = np.zeros([n_simulations,n_years+1])
r_sim[:,0] = r0 #Sets the first column (the initial value of each simulation) to r(0)


for i in range(n_years):
    r_sim[:,i+1] = vasi_mean(r_sim[:,i],t[i],t[i+1]) + np.sqrt(vasi_var(t[i],t[i+1]))*Z[:,i]

s_mean = np.exp(-alpha*t)*r0 + b*(1-np.exp(-alpha*t))