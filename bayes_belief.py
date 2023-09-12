import numpy as np

variables = {
    'A': ['True', 'False'],
    'B': ['True', 'False'],
    'C': ['True', 'False']
}

p_A = np.array([0.6, 0.4])

p_B = np.array([0.7, 0.3])


p_C_given_AB = np.array([

    [0.9, 0.1],

    [0.6, 0.4],

    [0.3, 0.7],

    [0.1, 0.9]
])


network_structure = {
    'A': ['C'],
    'B': ['C']
}

def joint_probability(A, B, C):
    i_A = variables['A'].index(A)
    i_B = variables['B'].index(B)
    i_C = variables['C'].index(C)
    return p_A[i_A] * p_B[i_B] * p_C_given_AB[i_A * 2 + i_B][i_C]

A = 'True'
B = 'False'
C = 'True'
probability = joint_probability(A, B, C)
print(f'P(A={A}, B={B}, C={C}) = {probability:.3f}')
