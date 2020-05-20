# Vasicek Bond prices
def A(t1,t2):
    return (1-np.exp(-alpha*(t2-t1)))/alpha

def C(t1,t2):
    val1 = (t2-t1-A(t1,t2))*(sigma**2/(2*alpha**2)-b)
    val2 = sigma**2*A(t1,t2)**2/(4*alpha)
    return val1-val2

def bond_price(r,t,T):
    return np.exp(-A(t,T)*r+C(t,T))

vasi_bond = bond_price(r0,0,t)