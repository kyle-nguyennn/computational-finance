# Plotting the yields
plt.plot(t[1:],bond_yield*100)
plt.plot(t[1:],mont_yield*100,'.')
plt.plot(t[1:],squad_yield*100,'x')
plt.plot(t[1:],trap_yield*100,'^')
plt.show()