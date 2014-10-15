from utils import updateDataset,buildDataset,buildRecurrentNetwork,loadRecurrentNetwork
from pybrain.supervised.trainers.rprop import RPropMinusTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

#nn=buildRecurrentNetwork()
nn=loadRecurrentNetwork('recurrentNetwork.xml')
dataset=buildDataset()

trainer=RPropMinusTrainer(nn)
trainer.setData(dataset)
print 'dataset set for trainer'
trainer.trainUntilConvergence()
print 'trained to convergence'


NetworkWriter.writeToFile(nn,'recurrentNetwork.xml')
