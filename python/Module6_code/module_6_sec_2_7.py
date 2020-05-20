# Determining yields
bond_yield = -np.log(bond_vec[1:])/t[1:]
mont_yield = -np.log(ZCB_prices[1:])/t[1:]
squad_yield = -np.log(squad_prices[1:])/t[1:]
trap_yield = -np.log(trap_prices[1:])/t[1:]