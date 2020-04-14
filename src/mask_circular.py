import numpy as np

#plain complex amplitude for a circular pupil
def p2p_circular(pupain):
    pupa=np.copy(pupain)
    nx,ny=np.shape(pupa)
    for i in range(0,nx):
        for j in range(0,ny):
            if (i-nx/2)**2+(j-ny/2)**2>nx**2/4:
                pupa[i,j]=0.0+0.0j
    return pupa

