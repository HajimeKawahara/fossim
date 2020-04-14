import numpy as np

#plain complex amplitude for a gaussian pupil
def p2p_gaussian(pupain,sigma):
    pupa=np.copy(pupain)
    nx,ny=np.shape(pupa)
    for i in range(0,nx):
        for j in range(0,ny):
            r2=(i-nx/2)**2+(j-ny/2)**2
            if r2>nx**2/4:
                pupa[i,j]=0.0+0.0j
            else:
                pupa[i,j]=pupa[i,j]*np.exp(-r2/(2.0*sigma*sigma))
                
    return pupa

