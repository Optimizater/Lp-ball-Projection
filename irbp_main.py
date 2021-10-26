#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:26:31 2021

@author: Xiangyu Yang
"""

import numpy as np
import random

import data_loader
import run_irbp_lib




if __name__ == '__main__':
    
    np.random.seed(1)
    random.seed(1)
    
    data_dim = np.intc(1e3) # user-specified
    
    p = 0.5
    radius = 1. # radius of the lp-ball
    point_to_be_projected = data_loader.point_projected(data_dim) # follow from N~(0,radius/data_dim)
    
    x_irbp = run_irbp_lib.get_sol(point_to_be_projected,p,radius)
    
    
        
        
    