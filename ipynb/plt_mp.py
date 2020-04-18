import pylab
import matplotlib.pyplot as plt
import numpy as np

def plotpup(pupa,filename="pupil_lat.png",small=False):

    if small:
        fig = plt.figure(figsize=(5,5))
    else:
        fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111)
    q=ax.imshow(np.abs(pupa))
    plt.title("amplitude")
    plt.colorbar(q)
    plt.savefig(filename)
    plt.show()

def plotfoc1D(foca,foca_perfect,exprat,filename="foc1D.png",ymin=10**-5):
    nx,ny=np.shape(foca)
    ifocal=np.abs(foca)**2
    ifocal_perfect=np.abs(foca_perfect)**2
    
    fig=plt.figure(figsize=(10,3.5))
    ax=fig.add_subplot(121)
    plt.plot(ifocal[int(nx/2),:]/np.max(ifocal),label="Multi pupil")
    plt.plot(ifocal_perfect[int(nx/2),:]/np.max(ifocal_perfect),label="Perfect Circular")
    plt.legend()
    plt.yscale("log")
    Q=300
    plt.xlim(nx/2-Q*exprat,nx/2+Q*exprat)
    plt.ylim(ymin,3.0)
    ax=fig.add_subplot(122)
    plt.plot(ifocal[int(nx/2),:]/np.max(ifocal),label="Multi pupil")
    plt.plot(ifocal_perfect[int(nx/2),:]/np.max(ifocal_perfect),label="Perfect Circular")
    plt.legend()
    plt.yscale("log")
    Q=10
    plt.xlim(nx/2-Q*exprat,nx/2+Q*exprat)
    plt.ylim(ymin,3.0)    
    plt.savefig(filename)
    plt.show()
    
def plotfoc2D(foca,exprat,filename="foc2D.png"):
    nx,ny=np.shape(foca)
    ifocal=np.abs(foca)**2    
    fig=plt.figure(figsize=(10,10))
    ax=fig.add_subplot(121)
    a=ax.imshow(np.log10(ifocal/np.max(ifocal)),vmin=-4,vmax=0,cmap="afmhot")
    plt.xlim(nx/2-150*exprat,nx/2+150*exprat)
    plt.ylim(ny/2-150*exprat,ny/2+150*exprat)
    #plt.colorbar(a)
    plt.title("Square amplitude at a Focal Plane")
    ax=fig.add_subplot(122)
    a=ax.imshow(np.log10(ifocal/np.max(ifocal)),vmin=-4,vmax=0,cmap="afmhot")
    #plt.colorbar(a)
    nx=foca.shape[0]
    ny=foca.shape[1]
    plt.xlim(nx/2-5*exprat,nx/2+5*exprat)
    plt.ylim(ny/2-5*exprat,ny/2+5*exprat)
    plt.title("Square amplitude at a Focal Plane")
    plt.savefig(filename)
    plt.show()
