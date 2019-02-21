#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:35:04 2019

@author: lmunier

This file is supposed to test the module to check if a matrix is square magic.
"""

import matplotlib.pyplot as plt
import is_magic_square_matrix
import numpy as np

def ex1():
    m = np.matrix('1 2; 3 1; 2 3')
    
    print(is_magic_square_matrix.isMagicSquareMatrix(m))
    return
    

def ex2():
    x = np.linspace(0, 2, 201)
    func = np.sin(x - 2)*np.exp(-np.power(x,2))
    
    plt.plot(x, func)
    plt.xlabel('x in [0,2]')
    plt.ylabel('sin(x-2)*exp(-x^2)')
    plt.axis('tight')
    
    plt.show()

    return
    
if __name__ == "__main__":
    ex2()