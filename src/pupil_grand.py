import numpy as np

def p2p_grand_phase_powerlaw(pupa,var_field=np.pi/8.0,alpha=-3,rmin=None,rmax=10.0):
    # fk = r**-alpha (rmin < k < rmax)
    # for k < rmin: fk=rmin**-alpha
    # else: 0
    n=len(pupa)
    if rmin is None:
        rmin=n/2
    
    fk=fpower(n,alpha,rmin,rmax,var_field=var_field)  
    d=phase_averration_grand(n,fk)
    pupa=pupa*np.exp(d*(1j))

    return pupa


def phase_averration_grand(n,fk):
    mu=0.0
    sigma=1.0
    a = np.random.normal(mu, sigma, n*n).reshape(n,n)
    b = np.random.normal(mu, sigma, n*n).reshape(n,n)
    a=a*np.sqrt(fk/2)
    b=b*np.sqrt(fk/2)
    c=a+b*(1j)
    d=np.fft.irfft2(np.fft.ifftshift(c)[:,0:int(n/2)+1])*n*n
    print (d.shape)
    #この値は実現値なのでlow frequency成分が多いと必ずしもinputに近くない
    return d

#power law fk
def fpower(nd,alpha,rmin,rmax,var_field=1):
    #sigma: sigma of the field
    rm=rmat(nd)
    f=rm**(alpha)
    maskmin=(rm<=rmin)
    f[maskmin]=rmin**(alpha)
    maskmax=(rm>rmax)
    f[maskmax]=0.0
    var=np.sum(f)#/(nd*nd)
    f=f/var*var_field
    return f

#distance matrix r
def rmat(n):
    if np.mod(n,2)==0:
        c=np.linspace(-n/2,n/2-1,n)
    else:
        c=np.linspace(-(n-1)/2,(n-1)/2,n)
    rmat=np.sqrt((c**2+c[:,np.newaxis]**2))
    return rmat
