##

import numpy as np
import scipy
from scipy import stats


def sample_1(N):
	return np.random.choice([-10, -5, 3, 9], size = N, p = [0.1, 0.4, 0.2, 0.3])

def sample_2(N):
	return scipy.stats.expon(0.5).rvs(N)


def get_mean(sampling_fun, N, M):
	for i in range(M):
		lista = sampling_fun(N)
		return np.mean(lista)

M = 10000
N = [10, 100, 1000]

for i in N:
	n = str(i)
	
	a = get_mean(sample_1, i, M)
	np.savetxt('sample_1_'+n+'.txt', a)

	b = get_mean(sample_2, i, M)
	np.savetxt('sample_2_'+n+'.txt', b)



	
	
