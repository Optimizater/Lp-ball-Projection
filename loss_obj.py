#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:51:01 2021

@author: Xiangyu Yang
"""

from numpy import linalg as LA

def least_square_loss(x, y) -> float:
    """
    Args:
        x : The current solution of dimension n by 1. 
        y : The given point to be projected

    Returns:
        The Objective value of the lp-ball projection problem, i.e., 0.5 * || x-y ||_2.
    
    """
    return 0.5 * LA.norm(x - y, 2)