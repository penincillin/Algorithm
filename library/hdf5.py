import os, sys, shutil
import numpy as np
import h5py
import sklearn
import sklearn.datasets
import sklearn.cross_validation

import pandas as pd

X, y = sklearn.datasets.make_classification(
    n_samples=10000, n_features=4, n_redundant=0, n_informative=2, 
    n_clusters_per_class=2, hypercube=False, random_state=0
)

# Split into train and test
X, Xt, y, yt = sklearn.cross_validation.train_test_split(X, y)


train_filename = '/devdata/software/caffe/caffe_origin/examples/hdf5_classification/train.h5'
test_filename = '/devdata/software/caffe/caffe_origin/examples/hdf5_classification/test.h5'


#Xt = X.transpose()
#yt = y.transpose()


X = X.astype(np.float32)
y = y.astype(np.float32)
Xt = Xt.astype(np.float32)
yt = yt.astype(np.float32)


'''
X = X.transpose()
y = y.transpose()
Xt = Xt.transpose()
yt = yt.transpose()
'''

print X.shape, y.shape


f = h5py.File(train_filename, 'w')
f.create_dataset('data', data=X)
f.create_dataset('label', data=y)
f.close()

f = h5py.File(test_filename, 'w')
f.create_dataset('data', data=Xt)
f.create_dataset('label', data=yt)
f.close()
