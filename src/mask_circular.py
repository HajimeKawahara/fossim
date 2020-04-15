import numpy as np

#plain complex amplitude for a circular pupil
def p2pm_circular(pupain,center=None,radius=None):
    pupa=np.copy(pupain)
    nx,ny=np.shape(pupa)
    y=np.array(range(ny))*np.array([np.ones(nx)]).T
    x=(np.array(range(nx))*np.array([np.ones(ny)]).T).T
    if center==None:
        center=[[nx/2],[ny/2]]
    center=np.array(center)
    ncirc=np.shape(center)[1]

    if radius==None:
        radius=[nx/2]
    elif type(radius)==int or type(radius)==float :
        radius=np.ones(ncirc)*radius        
    radius=np.array(radius)

    mask=np.zeros((nx,ny),dtype=np.bool)
    for i in range(0,ncirc):
        mask=mask | ((x-center[0,i])**2+(y-center[1,i])**2<radius[i]**2)

    mask=~mask
    return mask

