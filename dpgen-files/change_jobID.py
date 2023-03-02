import os
import numpy as np

counter=0
list_dir = os.listdir('.')
for item in list_dir:
	if len(item) >=36:
		os.chdir(item)
		rand_job = np.random.randint(100000,999999)
		os.system(f'echo {rand_job} > {item}_job_id')
		os.system('cat *job*')
		os.chdir('../')
