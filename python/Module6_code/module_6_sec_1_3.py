# Plotting the results
t_graph = np.ones(r_sim.shape)*t
plt.plot(np.transpose(t_graph),np.transpose(r_sim*100),'r')
plt.plot(t,s_mean*100)
plt.show()