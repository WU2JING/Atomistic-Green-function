import numpy as np
from math import pi
import scipy.io

def decimate(H00: np.ndarray,
             H01: np.ndarray,
             w: float):
    w2I = (w**2 + 1.j * 0.0001) * np.eye(360)
    s = H00
    e = H00
    a = H01
    tol = 1
    while tol > 1e-6:
        g = np.linalg.inv(w2I - e)
        b = a.T
        agb = a @ g @ b
        s = s + agb
        e = e + agb + b @ g @ a
        a = a @g @ a
        tol = np.linalg.norm(a)
    return np.linalg.inv(w2I - s)

def compute_T(w, HC, HCL, HCR, H00L, H01L, H00R, H01R):
    gsR = decimate(H00R, H01R, w)
    gsL = decimate(H00L, H01L, w)
    SigmaR = HCR @ gsR @ HCR.conj().T
    SigmaL = HCL @ gsL @ HCL.conj().T
    w2 = w * w
    G = np.linalg.inv(w2 * np.eye(360) - HC - SigmaL - SigmaR)
    M1 = 1.j * (SigmaL - SigmaL.conj().T)
    M2 = 1.j * (SigmaR - SigmaR.conj().T)
    
    T = np.trace(M1 @ G @ M2 @ G.conj().T).real
    print(w, T)

nu = np.arange(0.2, 52.0, 0.2)
omegas = nu * 2 * 3.14159265 * 10.18 / 1000
H_C =  np.load('H_C.npy')
H_CL = np.load('H_CL.npy')
H_CR = np.load('H_CR.npy')
H_00L = np.load('H_00L.npy')
H_01L = np.load('H_01L.npy')
H_00R = np.load('H_00R.npy')
H_01R = np.load('H_01R.npy')

for i in omegas:
    compute_T(round(i,6), H_C, H_CL, H_CR, H_00L, H_01L, H_00R, H_01R)

