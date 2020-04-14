import numpy as np

def p2p_deformable_mirror(pupa, a, dim_ao):	
	n = len(pupa)
	ao_size = n/dim_ao
	ao_phase = np.exp(1j*a)
	ao_phase = np.repeat(ao_phase, ao_size, axis=0)
	ao_phase = np.repeat(ao_phase, ao_size, axis=1)
	return pupa * ao_phase


def p2p_sinc_sinc_sin(pupa, dim_ao, P, delta_xi, delta_eta, xi_c, theta):
	n = len(pupa)
	ao_size = n/dim_ao
	if np.mod(ao_size,2)==0:
		c=np.linspace(-dim_ao/2,dim_ao/2-1,dim_ao) * ao_size
	else:
		c=np.linspace(-(dim_ao-1)/2,(dim_ao-1)/2,dim_ao)  * ao_size
	phi =  P *np.sinc(c* delta_xi)*np.sin(xi_c * c +np.ones(dim_ao) * theta) *np.sinc(delta_eta *  c[:,np.newaxis])
	ao_phase = np.exp(1j*phi)
	ao_phase = np.repeat(ao_phase, ao_size, axis=0)
	ao_phase = np.repeat(ao_phase, ao_size, axis=1)
	return np.imag(ao_phase), pupa * ao_phase
	