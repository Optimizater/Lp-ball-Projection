#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:51:01 2021

@author: Xiangyu Yang
"""

from numpy import linalg as LA

def least_square_loss(projection_point, point_to_be_projected):
    """
    Args:
        projection_point : The current solution of dimension n by 1. 
        point_to_be_projected : The given point to be projected

    Returns:
        The Objective value of the lp-ball projection problem, i.e., 0.5 * || x-y ||_2.
    
    """
    return 0.5 * LA.norm(projection_point - point_to_be_projected, 2)
