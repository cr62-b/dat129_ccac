# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:56:21 2020

@author: CRohal
"""

# Build a Neural Network using a numpy
# https://enlight.nyc/projects/neural-network
# An introduction to building a basic feedforward neural network with
# backpropagation in Python.
# The program has an array (x_all) of hours studying and hours sleep.  The
# last list in the array is the test data.  It has and array (y) with are the
# test results.
# https://numpy.org/doc/stable/user/whatisnumpy.html

import numpy as np
import matplotlib.pyplot as plt

# X = (hours studying, hours sleeping), y = score on test
x_all = np.array(([2, 9], [1, 5], [3, 6], [5, 10]), dtype=float) # input data
y = np.array(([92], [86], [89]), dtype=float) # output

x_raw_data = np.split(x_all, [3])[1] # testing data

# scale units
x_all = x_all/np.amax(x_all, axis=0) # scaling input data by dividing all numbers by the highest value
y = y/100 # scaling output data (max test score is 100)

# split data
X = np.array_split(x_all, [3])[0] # training data
x_predicted = np.split(x_all, [3])[1] # testing data

class neural_network(object):
  def __init__(self):
  #parameters
    self.inputSize = 2
    self.outputSize = 1
    self.hiddenSize = 3

  #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):
    print("Predicted data based on trained weights: ")
    print("Input: " + str(x_raw_data))
    print("Input (scaled): " + str(x_predicted))
    print("Output: " + str(100*self.forward(x_predicted)))

# A real time graph for how the neural network learns.
# Within our for loop, we can append our iteration into the count list and the
# loss output to the loss list. This can be plotted in real-time by first
# clearing the plot using plt.cla() and then calling the plt.plot(count, loss)
# function. We can also set a title using plt.title() and labels using
# plt.xlabel() , and plt.ylabel(). Lastly, we call plt.pause(.001) to specify
# how long the program should wait before plotting the data again.
def network():
    nn = neural_network()
    count = [] # list to store iteration count
    loss = [] # list to store loss values
    for i in range(10): # trains the nn 1,000 times
      print("# " + str(i) + "\n")
      print("Input (scaled): \n" + str(X))
      print("Actual Output: \n" + str(y))
      print("Predicted Output: \n" + str(nn.forward(X)))
      cost = str(np.mean(np.square(y - nn.forward(X))))
      print("Loss: \n" +  cost ) # mean squared error
      print("\n")
      count.append(i)
      loss.append(np.round(float(cost), 6))
      plt.cla() # clear plot
      plt.title("Loss over Iterations")
      plt.xlabel("Iterations")
      plt.ylabel("Loss")
      plt.plot(count, loss)
      plt.pause(.001)
      nn.train(X, y)
    return nn

def main():
    nn = network()
    nn.saveWeights()
    nn.predict()

main()








