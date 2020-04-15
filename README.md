# Fossim

Fourier Optics Simple Simulator

pupil <-> focal simulation

## variables
- pupa (pupil array): complex amplitude array at a pupil. [numpy.complex]
- foca (focal plane array): complex amplitude at a focal plane. [numpy.complex]
- pupil mask (pupil mask): mask for pupa [boolen]

## functions (currently we consider a pupil and a focal plane only)

- wave generator: (wg_)             -> pupa (function: generating wave)
- pupil disturber: (p2p_):     pupa -> pupa (function: multiplying complex variables)
- coronagraph function (cf_):  pupa -> foca (function: coronagraph including FT) 


p2p includes pupil aberration, telescope masking, DM function at pupil, etc.

## coronagraph functions

-mask_circular.py (no coronagraph)
-visible nuller.py
-mask_gaussian.py (pupil apodization)
