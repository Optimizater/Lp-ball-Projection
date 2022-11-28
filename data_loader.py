#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:32:16 2021

@author: Xiangyu Yang
"""

import numpy as np

def point_projected(n: int):
    """Generates the point to be projected

    Args:
        n (int): [The length of the point to be projected.]

    Returns:
        data (float): [The point to be projected, following the standard Normal distribution.]
    """    
    
    mu, sigma = 0., 1. 

    return np.random.normal(mu,sigma,n)
