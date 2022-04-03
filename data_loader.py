#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:32:16 2021

@author: Xiangyu Yang
"""

import numpy as np

def point_projected(n: int) -> float:
    """AI is creating summary for point_projected

    Args:
        n (int): [The length of the point to be projected.]

    Returns:
        data (float): [The point to be projected, following the standard Normal distribution.]
    """    
    
    mu, sigma = 0., 1. 
    data = np.random.normal(mu,sigma,n)

    return data