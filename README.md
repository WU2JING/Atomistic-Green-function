This is an example of atomic Green's function solving for graphene's phonon transmission. Below are the detailed steps.
1. Calculate harmonic force constant using phonopy. ----> FORCE_CONSTANTS
2. Convert SPOSCAR files to lammps format (data file) and divide the system into three regions (left lead, scattering region, and rightlead) according to your system.  ----> layer_map
3. Run the script hm.py to obtain the interaction matrix.
4. Run the script agf.py to obtain the phonon transmission.
5. There are good reference links here. (https://github.com/brucefan1983/AGF-phonon-transport and https://github.com/araghukas/agf/tree/main/agf)
6. Any discussion is welcomed. (email: wujing_53@163.com)
7. Warning! Warning! Warning! This is just an example of the phonon Green's function.

