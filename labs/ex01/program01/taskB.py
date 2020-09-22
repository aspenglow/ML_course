import numpy as np

def pairwiseDistance(P, Q):
    p = P.shape[0]
    q = Q.shape[0]
    D = np.zeros(p,q)
    for i in range(p):
        for j in range(q):
            distance = ((P[i,0] - Q[j,0])**2 + (P[i,1] - Q[j,1])**2 )**0.5
            D[i,j] = distance
    
    return D

