# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:08:27 2021

@author: Viviana Paloma, José Manuel
"""
import numpy as np

def gradient(x, A, b):
 element_1 = np.dot(np.transpose(A),np.dot(A, x))
 element_2 = np.dot(np.transpose(A), b)
 return element_1 - element_2


#def linear_solve(A, b, x_start, umbral = 0.001, max_iter = 1000)
###
#x_nuevo = x_viejo - k * Gradiente 

A_coef = np.array([[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]])
b_coef = np.array([7.0, -19.0, 4.0])

x_sol = np.array([1.0, 1.0, 1.0])

    
def linear_solve(M, v, x_start, u, m_i):
    k = 0.002
    for i in range(m_i):
        print(x_start)
        x_start = x_start - k * gradient(x_start, M, v)
        current_v = np.dot(M,x_start)
        error_np = np.sum(np.abs(current_v-v))
        if error_np < u:
            return x_start

print(linear_solve(A_coef, b_coef, x_sol, 0.00001, 10000))