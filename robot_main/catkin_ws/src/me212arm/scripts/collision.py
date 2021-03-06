#!/usr/bin/python

from planner import fk1, fk
import numpy as np

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def in_collision(q, obstacle_segs):
    arm_segments = [( (0,0), fk1(q) ), ( fk1(q), fk(q))]
    
    final_val = False
    for obs in obstacle_segs:
        for arm in arm_segments:    
            inter = intersect(arm[0],arm[1],obs[0],obs[1])
            final_val = final_val or inter
    
    return final_val
        
    ## return True if there are segments from arm_segments and segments from obstacle_segs intersect

if __name__=="__main__":
    
    obstacle_segs = [ [[0.0,0.0], [0.0,0.4]] ]  # line segs ((x1,z1)--(x2,z2))
    print in_collision( [0,0], obstacle_segs)                       # False
    print in_collision( [np.pi /4, -np.pi *3/4], obstacle_segs)     # True
    print in_collision( [-0.45709828817786735, -1.4971869034039356], obstacle_segs) # False
