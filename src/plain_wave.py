import numpy as np
import matplotlib.pyplot as plt

def wg_plain_wave(n,pos_theta):
    phase=make_tiptilt_phase(n,pos_theta)
    return np.exp(phase*(1j))
    
def make_tiptilt_phase(n,pos_theta):
    a=np.tile(np.linspace(0.0,1.0,n),(n,1))
    phase=2*np.pi*((a*pos_theta[0]) + np.transpose(a*pos_theta[1]))
    #the unit of pos_theta is [radian]
    return phase


if __name__ == "__main__":

    arcsectorad=np.pi/60.0/60.0/180.0
    theta=0.01*arcsectorad  #10mas
    wavelength=1.0e-6 # 1 micron
    diameter=30.0 # 30 meter
    tilt=theta*diameter/wavelength # in unit of l/d

    pupa=wg_plain_wave(512,[0.0,tilt])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    q=ax.imshow(np.angle(pupa))
    plt.title("phase of pupil array [rad]")
    plt.colorbar(q)
    plt.show()
