# Closed-form bond prices
bond_vec = bond_price(r0,0,t)

# Plotting bond prices
plt.plot(t,bond_vec) # Analytical solution
plt.plot(t,ZCB_prices,'.') # Simulated Yt and rt
plt.plot(t,squad_prices,'x') #Simulated rt and estimated Yt
plt.plot(t,trap_prices,'^') #Simulated rt and estimated Yt
plt.show()