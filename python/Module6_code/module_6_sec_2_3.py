# Functions for means, variances, and correlations
def Y_mean(Y,r,t1,t2):
    return Y + (t2-t1)*b+(r-b)*A(t1,t2)

def Y_var(t1,t2):
    return sigma**2*(t2-t1-A(t1,t2)-alpha*A(t1,t2)**2/2)/(alpha**2)

def rY_var(t1,t2):
    return sigma**2*(A(t1,t2)**2)/2

def rY_rho(t1,t2):
    return rY_var(t1,t2)/np.sqrt(vasi_var(t1,t2)*Y_var(t1,t2))