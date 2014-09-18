from pybrain.datasets import SupervisedDataset
from pybrain.tools.shortcuts import buildNetwork
dataset = SupervisedDataset(8,2)
# coding: utf-8
validIn = [0.33333,0.25,0.04167,0.04,0.11111,0.08333,1.0,0.125]
validOut= [0,1]
dataset.addSample(validIn,validOut)
validIn = [0.03448,0.07143,0.25,0.03571,0.25,0.14286,0.06667,0.03125]
validOut = [1,0]
dataset.addSample(validIn,validOut)
validIn = [0.09091,0.03704,0.2,0.2,0.03226,0.03125,0.08333,0.09091]
dataset.addSample(validIn,validOut)
validIn = [0.04545,0.0625,0.33333,0.04348,0.06667,0.33333,0.05,0.05882]
dataset.addSample(validIn,validOut)
validIn = [0.04167,0.04348,0.125,0.05556,0.05556,0.03448,0.11111,0.04762]
validOut = [0,1]
dataset.addSample(validIn,validOut)
validIn = [0.03333,0.03226,0.03846,0.03448,0.5,1.0,0.03125,0.1]
dataset.addSample(validIn,validOut)
validIn = [0.04762,0.05882,0.09091,0.05,0.05,0.2,0.04,0.04545]
validOut = [1,0]
dataset.addSample(validIn,validOut)
validIn = [0.03571,0.05263,0.05263,0.11111,0.08333,0.5,0.03226,0.0625]
validOut = [0,1]
dataset.addSample(validIn,validOut)
nn=buildNetwork(4,3,2)
