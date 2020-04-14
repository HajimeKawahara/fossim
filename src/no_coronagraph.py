import numpy as np

def cf_no_coronagraph(pupain,exprat=4):
    # Coronagraph Function of No Coronagraph
    #oversampling and zero-padding
    nwide=exprat*np.array(pupain.shape)
    wtilpsi1=np.zeros(exprat*np.array(pupain.shape))*(0.0+0.0j)
    wtilpsi1[0:len(pupain),0:len(pupain)] = pupain
    #FFT
    f1=np.fft.fftshift(np.fft.fft2(wtilpsi1))
    foca = f1/np.sqrt(nwide[0]/nwide[1])

    return foca
