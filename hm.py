from enum import IntEnum
from typing import List
import numpy as np

def read_harmonic_constants(harmonic_constants_filename, d):
    with open(harmonic_constants_filename) as f:
        line = f.readline()
        n, m = [int(x) for x in line.split()]
        harmonic_constants = np.zeros((n, m, d, d), dtype=np.double)
        line = f.readline()
        atom_i, atom_j = [int(x) - 1 for x in line.split()]
        for i in range(d):
            line = f.readline()
            tmp_f = []
            for x in line.split():
               if abs(float(x)) < 1e-14:
                   tmp_f.append(0)
               else:
                   tmp_f.append(float(x)/12.01)
            harmonic_constants[atom_i][atom_j][i] = tmp_f 
        line = f.readline()
        while line:
            atom_i, atom_j = [int(x) - 1 for x in line.split()]
            for i in range(d):
                line = f.readline()
                tmp_f = []
                for x in line.split():
                    if abs(float(x)) < 1e-14:
                        tmp_f.append(0)
                    else:
                        tmp_f.append(float(x)/12.01)
                harmonic_constants[atom_i][atom_j][i] = tmp_f 
            line = f.readline()

    return harmonic_constants

def extract_matrix(row_index, col_index, arr):
    m = len(row_index) 
    n = len(col_index) 
    d = 3 
    matrix = np.zeros((m, n, d, d))

    i0 = 0
    for i in row_index:
        j0 = 0
        for j in col_index:
            matrix[i0][j0] = arr[i][j]
            j0 += 1
        i0 += 1
    return matrix

def unfold_matrix(arr):
    m, n, p, q = arr.shape
    new_arr = np.zeros((m * p, n * q), dtype=arr.dtype)

    for i in range(m):
        i0 = p * i
        for j in range(n):
            j0 = q * j
            for k in range(p):
                for l in range(q):
                    val = arr[i, j, k, l]
                    new_arr[i0 + k, j0 + l] = val
    return new_arr

def read_atoms(layer_map_file):
    with open(layer_map_file) as f:
        num = []
        tmp = []
        line = f.readline()
        while len(line) > 0:
            if line.startswith("layer") :
                if len (tmp) > 0:
                    num.append(tmp)
                    tmp = []
            else:
                ID = int(line.split()[0])
                tmp.append(ID-1)
            line = f.readline()
    num.append(tmp)
    return num

hcs = read_harmonic_constants('FORCE_CONSTANTS', 3)
atom_id = read_atoms('layer_map')
H_C  = unfold_matrix(extract_matrix(atom_id[2], atom_id[2], hcs))
H_CL = unfold_matrix(extract_matrix(atom_id[2], atom_id[1], hcs))
H_CR  = unfold_matrix(extract_matrix(atom_id[2], atom_id[3], hcs))
H_00L = unfold_matrix(extract_matrix(atom_id[1], atom_id[1], hcs))
H_01L = unfold_matrix(extract_matrix(atom_id[1], atom_id[0], hcs))
H_00R = unfold_matrix(extract_matrix(atom_id[3], atom_id[3], hcs))
H_01R = unfold_matrix(extract_matrix(atom_id[3], atom_id[4], hcs))
np.save('H_C.npy',H_C)
np.save('H_CL.npy',H_CL)
np.save('H_CR.npy',H_CR)
np.save('H_00L.npy',H_00L)
np.save('H_01L.npy',H_01L)
np.save('H_00R.npy',H_00R)
np.save('H_01R.npy',H_01R)
