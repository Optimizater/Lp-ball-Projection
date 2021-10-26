#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:32:16 2021

@author: Xiangyu Yang
"""

import numpy as np

def point_projected(N) -> float:
    '''Generate the point to be projected.
    
    Args: 
        N: the length of the point to be projected.
        
    Returns:
        data: The point follows the standard Normal distribution.
    '''
    
    mu, sigma = 0., 1. 
    data = np.random.normal(mu,sigma,N)
    
    return data