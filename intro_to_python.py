import numpy as np

print("#1------------------")

matrix1 = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        if i == j:
            matrix1[i][j] = 1

print(matrix1.astype(int))

print("#2------------------")

matrix2 = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        if i == j:
            matrix2[i][j] = 1
        else: matrix2[i][j] = 3

print(matrix2.astype(int))

print("#3------------------")

matrix3 = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        if i == j:
            matrix3[i][j] = 1
        else: matrix3[i][j] = 3

matrix3 = matrix3[:, :-1]
print(matrix3.astype(int))