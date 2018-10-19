
# coding: utf-8

# # Using FIt-SNE
# 
# Author: Dmitry Kobak

# In[1]:

import numpy as np
import pylab as plt
import seaborn as sns; sns.set()
from fast_tsne.core import tsne


# In[2]:


# Load MNIST data
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784).astype('float64') / 255
x_test  =  x_test.reshape(10000, 784).astype('float64') / 255
X = np.concatenate((x_train, x_test))
y = np.concatenate((y_train, y_test))
print(X.shape)

# Do PCA and keep 50 dimensions
X = X - X.mean(axis=0)
U, s, V = np.linalg.svd(X, full_matrices=False)
X50 = np.dot(U, np.diag(s))[:,:50]

# We will use PCA initialization later on
PCAinit = X50[:,:2] / np.std(X50[:,0]) * 0.0001

# 10 nice colors
col = np.array(['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99',
                '#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a'])


# In[4]:


# Running t-SNE on the full MNIST in the default way

Z = tsne(X50, perplexity=50, seed=42)

plt.figure(figsize=(5,5))
plt.scatter(Z[:,0], Z[:,1], c=col[y], s=1)
plt.tight_layout()
plt.show()