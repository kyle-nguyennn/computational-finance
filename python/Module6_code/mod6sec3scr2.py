# Applying the algorithms
np.random.seed(0)
n_simulations = 100000
n_steps = len(t)predcorr_forward = np.ones([n_simulations,n_steps-1])*(vasi_bond[:-1]-vasi_bond[1:])/(2*vasi_bond[1:])
predcorr_capfac = np.ones([n_simulations,n_steps])delta = np.ones([n_simulations,n_steps-1])*(t[1:]-t[:-1])