import numpy as np

def cf_vnuller_2beam(pupain,shearrate=0.2,exprat=4):
    # Coronagraph Function for a 2-beam visible nuller
    # shear rate: shear in unit of length of dimension[0] of a pupil array 
    pbs=int(shearrate*pupain.shape[0]/2)
    c1,m1=shiftpupa(pupain,[-pbs,0])
    c2,m2=shiftpupa(pupain,[pbs,0])
    cc1=m1*m2*(c1-c2)/2.0 #null pupil
    cc2=m1*m2*(c1+c2)/2.0 #bright pupil
    #oversampling and zero-padding
    nwide=exprat*np.array(pupain.shape)
    wtilpsi1=np.zeros(exprat*np.array(cc1.shape))*(0.0+0.0j)
    wtilpsi2=np.zeros(exprat*np.array(cc2.shape))*(0.0+0.0j)
    wtilpsi1[0:len(cc1),0:len(cc1)] = cc1
    wtilpsi2[0:len(cc2),0:len(cc2)] = cc2
    #FFT
    f1=np.fft.fftshift(np.fft.fft2(wtilpsi1))
    f2=np.fft.fftshift(np.fft.fft2(wtilpsi2))
    foca_null = f1/np.sqrt(nwide[0]*nwide[1])
    foca_bright = f2/np.sqrt(nwide[0]*nwide[1])

    return foca_null,foca_bright

def shiftpupa(pupain,nbase,val=0.0):
    i=0
    pupa=np.array(pupain)
    if val is None:
        pupa[pupa!=pupa]=0.0
        val=0.0

    mvpupa=np.roll(np.roll(pupa,nbase[1], axis=0), nbase[0], axis=1)
    maskx=maskroll(pupa.shape,nbase[0],1)
    masky=maskroll(pupa.shape,nbase[1],0)
    maskos=np.ones(pupa.shape)

    maskos[mvpupa==val]=0.0
    return maskx*masky*maskos*mvpupa,maskx*masky*maskos

def maskroll(shape,nbasex,ix):
    if nbasex==0:
        addmask=np.ones(shape)
    else:
        nx=shape[1]
        ny=shape[0]
        addmask=np.linspace(0, nx*ny-1, nx*ny).reshape(nx,ny)
        addmask=(np.roll(addmask, nbasex, axis=ix)-addmask)/abs(np.roll(addmask, nbasex, axis=ix)-addmask)
        if nbasex<0:
            addmask=(addmask-1.0)/2.0+1
        else:
            addmask=(-addmask+1.0)/2.0

    return addmask

if __name__ == "__main__":
    cf_vuller(None)
