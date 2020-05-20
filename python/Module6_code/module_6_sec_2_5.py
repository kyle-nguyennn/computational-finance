# Yt estimates
r_mat = np.cumsum(r_simtemp[:,0:-1],axis = 1)*(t[1:]-t[0:-1])
r_mat2 = np.cumsum(r_simtemp[:,0:-1] + r_simtemp[:,1:],axis = 1)/2*(t[1:]-t[0:-1]) 

# Bond price estimates
squad_prices = np.ones(n_years+1) #At time 0, bonds have a price of 1
trap_prices = np.ones(n_years+1) 

squad_prices[1:] = np.mean(np.exp(-r_mat),axis = 0)
trap_prices[1:] = np.mean(np.exp(-r_mat2),axis = 0)