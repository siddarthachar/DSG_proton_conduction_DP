# Deep Learning Potentials for Proton Transfer in Double-Sided Graphanol

Files that help readers perform DP-MD simulaitons, phonon calculations, and train DPs for double-sided graphanol (DSG) are provided. 

1. **DSG_dp.pb**: Protobuf Tensorflow file for DSG. 
2. **dsg-1p.lmp**: Initial lammps coordinate file for DSG. 
3. **in.lammps**: LAMMPS input file that uses DSG_dp.pb as the potential and dsg-1p.lmp as the initial sttucture to run DP-NVT MD simulations.
4. **phonolammps/**: Folder containing files needed to perform phonon calculations using DP. 
5. **dpgen-files/**: Folder containing files needed to train a new DP for DSG via the DP-GEN framework. 


