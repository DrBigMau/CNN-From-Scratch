# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 06:11:28 2024

@author: MMH_user
"""

import numpy as np
from MyANN import *

def ApplyMyANN(x_new):
    
    w1 = np.load('weights1.npy')
    w2 = np.load('weights2.npy')
    
    S = w1.shape
    
    b1 = np.load('bias1.npy')
    b2 = np.load('bias2.npy')
    
    dense1        = Layer_Dense(S[0], S[1])
    dense2        = Layer_Dense(S[1], 3)
    activation1   = Activation_ReLU()
    
    dense1.weights = w1
    dense2.weights = w2
    
    dense1.biases  = b1
    dense2.biases  = b2
    
    dense1.forward(x_new)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    result = dense2.output
    
    exp_values    = np.exp(result - np.max(result))
    probabilities = exp_values/np.sum(exp_values, axis = 1, \
                                      keepdims = True)
        
    predictions = np.argmax(probabilities, axis = 1)
    
    return(predictions)
    
    
    
    
    
    