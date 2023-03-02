import numpy as np
import matplotlib.pyplot as plt
import sys

iter_path = str(sys.argv[1])
models = ['000','001','002','003']

for m in models:
	data = np.loadtxt(f'{iter_path}/{m}/lcurve.out')
	plt.plot(data[:,0], data[:,2], label = f'{m}')
plt.title('RMSE energy')
plt.xlabel('step')
plt.ylabel('rmse_e_trn')
plt.legend(frameon=False)
plt.savefig(f'{iter_path}/rmse_e_trn.png')
plt.clf()

for m in models:
	data = np.loadtxt(f'{iter_path}/{m}/lcurve.out')
	plt.plot(data[:,0], data[:,3], label = f'{m}')
plt.title('RMSE force')
plt.xlabel('step')
plt.ylabel('rmse_f_trn')
plt.legend(frameon=False)
plt.savefig(f'{iter_path}/rmse_f_trn.png')