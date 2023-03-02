# Integration with phonopy
from phonolammps import Phonolammps
from phonopy import Phonopy
import matplotlib.pyplot as plt
import numpy as np
import phonopy

print("HI")
phlammps = Phonolammps('in.lammps',
                       supercell_matrix=[[3, 0, 0],
                                         [0, 3, 0],
                                         [0, 0, 1]])
print("HI")
unitcell = phlammps.get_unitcell()
# force_constants = phlammps.get_force_constants()
supercell_matrix = phlammps.get_supercell_matrix()
phh = phonopy.load(phonopy_yaml='phonopy_params.yaml')
force_constants = phh.force_constants
phonon = Phonopy(unitcell,
                 supercell_matrix)

phonon.set_force_constants(force_constants)
# print(phonon)
phonon.save(settings={'force_constants': True})
# use https://phonolammps.readthedocs.io/en/master/starting.html command prompt to get FORCE_SET using DP

# phonon.run_mesh([33, 33, 1], with_eigenvectors=True, is_mesh_symmetry=False)
# phonon.run_projected_dos(sigma=1)
# phonon.plot_projected_dos().show()
# phonon.write_projected_dos('projectedDOS.dat')
# p_projected = phonon.get_projected_dos_dict()

# phonon.auto_projected_dos(filename='auto_projected_dos.dat')

# print(p_projected)
# print(p)
#np.savetxt("pdos-pl.txt",p)
#pp = np.loadtxt("total_dos_vasp.dat")
# plt.plot(p['frequency_points'],p['total_dos'],label = 'DP')
# #plt.plot(pp[:,0], pp[:,1],label='VASP')
# plt.legend()
# plt.xlabel("Frequency")
# plt.ylabel("VDOS")
# plt.grid()
# #plt.xlim(0,120)

# plt.savefig("pdos-dp-oneside.png")

# plt.show()

# tot = p['total_dos']
# freq = p['frequency_points']

# out = open("plammps-totpdso-oneside.txt",'w+')

# for i in range(len(p['total_dos'])):
# 	out.write(str(freq[i])+"\t"+str(tot[i])+"\n")




#phonon.plot_total_DOS().show()

# phonon.set_thermal_properties()
# out_tp = open('plammps-tp-oneside.txt','w+')

# tp_dict = phonon.get_thermal_properties_dict()
# temperatures = tp_dict['temperatures']
# free_energy = tp_dict['free_energy']
# entropy = tp_dict['entropy']
# heat_capacity = tp_dict['heat_capacity']

# for i in range(len(temperatures)):
# 	out_tp.write(str(temperatures[i])+"\t"+str(free_energy[i])+"\t"+str(entropy[i])+"\t"+str(heat_capacity[i])+'\n')


# #phonon.set_thermal_properties()
# phonon.plot_thermal_properties().show()
