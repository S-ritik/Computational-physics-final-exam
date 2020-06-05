# Q9 - To obtain singular values

import numpy as np
import scipy.linalg as sl

a=np.array([[2,1],[1,0],[0,1]])  # Given first matrix
Ua, sa, Vha = sl.svd(a,full_matrices=False)
print("Singular values of first matrix are ",sa)

b=np.array([[1,1,0],[1,0,1],[0,1,1]]) # Given second  matrix
Ub, sb, Vhb = sl.svd(b)
print("Singular values of second matrix are ",sb)
