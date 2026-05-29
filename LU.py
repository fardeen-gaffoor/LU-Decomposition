# To print L and U matrix
'''Program to find L and U matrix using LU decomposition.
Developed by: Fardeen Gaffoor S
RegisterNumber: 212225230068
'''
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

import numpy as np
from scipy.linalg import lu
import ast

matrix = np.array(ast.literal_eval(input()), dtype=float)
P, L, U = lu(matrix)
print(L)
print(U)
#add the code to get the L and U matrix


# To print X matrix (solution to the equations)
'''Program to solve a matrix using LU decomposition.
Developed by: Fardeen Gaffoor S
RegisterNumber: 212225230068
'''

# To print X matrix (solution to the equations)
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

import numpy as np
from scipy.linalg import lu_factor, lu_solve
import ast

A = np.array(ast.literal_eval(input()), dtype=float)
b = np.array(ast.literal_eval(input()), dtype=float)

lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)
print(x)
#add the code to get the solution of the matrix

