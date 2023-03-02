import numpy as np
import os

list_dir = os.listdir('.')
job_list = [x for x in list_dir if len(x) >= 36]
count = 0
for j in job_list:
	if f'{j}_tag_finished' in os.listdir(j):
		count+=1
print(f'{count}/{len(job_list)} finished')
	
