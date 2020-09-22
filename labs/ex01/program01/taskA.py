import numpy as np

def matrixNormalization(x):
    d = x.shape[1]
    for i in range(d):
        mean = np.mean(x[:,i])
        stdvar = np.std(x[:,i])
        x[:,i] = (x[:,i] - mean)/stdvar
        print("mean %f  var %f:" % (np.mean(x[:,i]), np.std(x[:,i])))
    return x


if __name__ == "__main__":
    x = np.array([[1.,2.],[2.,3.],[3.,4.]])
    p = matrixNormalization(x)