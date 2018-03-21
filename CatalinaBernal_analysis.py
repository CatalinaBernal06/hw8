import numpy as np
import matplotlib.pyplot as plt
import os

def normal_dist(x, mean, sigma):
	return np.random.normal(mean, sigma, x)

def get_fit(filename):
	data = np.loadtxt(filename)
	plt.figure()
	plt.hist(data)
	plt.savefig(filename + '.png')

lista_dir = os.listdir('/home/administrador/Desktop')

for arc in lista_dir:
	get
