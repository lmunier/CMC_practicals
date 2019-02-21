#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:35:04 2019

@author: lmunier

This file contain a script to compute if a matrix is a magic square one or not.

return true if the matrix is a magic square one.
returnfalse if it is not.
"""

import numpy as np

def isMagicSquareMatrix(M):
    shape = M.shape
    
    if(shape[0] != shape[1]):
        return False
    else:
        magic_sum = M.sum(axis=1)
        
        for i in range(2):
            if(i == 0):
                magic_number = magic_sum[i]
            
            for j in magic_sum:
                if(j != magic_number):
                    return False
        
    return True