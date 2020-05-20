# Useful functions
def vasi_mean(r,t1,t2):
    """Gives the mean under the Vasicek model. Note that t2 > t1. r is the
    interest rate from the beginning of the period"""
    return np.exp(-alpha*(t2-t1))*r+b*(1-np.exp(-alpha*(t2-t1)))

def vasi_var(t1,t2):
    """Gives the variance under the Vasicek model. Note that t2 > t1"""
    return (sigma**2)*(1-np.exp(-2*alpha*(t2-t1)))/(2*alpha)