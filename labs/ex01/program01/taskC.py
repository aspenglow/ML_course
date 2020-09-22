import numpy as np
import math


def likelihood(data, mean1, cov1, mean2, cov2):
    N = data.shape[0]
    a = np.zeros(N)
    for i in range(N):
        p1 = gaussianDistributions(data[i,:], mean1, cov1)
        p2 = gaussianDistributions(data[i,:], mean2, cov2)
        if p1 > p2:
            a[i] = 1
        else:
            a[i] = 2
    return a


def gaussianDistributions(x, mean, cov):
    d = mean.shape[0]
    det = np.linalg.det(cov)
    inverse = np.linalg.inv(cov)
    upexp = -0.5 * (x-mean).dot(inverse.dot(x-mean))
    p = np.exp(upexp) / ((2*math.pi)**(d/2) * det**0.5)
    return p

if __name__ == "__main__":
   data = np.array([[6,9,2],[1,4,4],[9,3,1],[8,2,6]])
   mean1 = np.array([3,5,7])
   mean2 = np.array([2,6,9])
   cov1 = np.array([[1,7,3],[2,5,8],[3,7,6]])
   cov2 = np.array([[2,6,9],[5,3,7],[2,8,6]])
   a = likelihood(data, mean1, cov1, mean2, cov2)
   print(a)