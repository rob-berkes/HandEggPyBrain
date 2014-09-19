from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.neuralnets import NNregression
from lib import team
from utils import buildTeamlist
teamlist=buildTeamlist()

from pybrain.datasets import SupervisedDataSet
dataset=SupervisedDataSet(8,2)
yearlist=['2013','2014']
for year in yearlist:
  fnameHead=str(year)+'/week'
  fnameTail='.csv'
  try:
    for week in range(1,17):
      fnameOpen = fnameHead+str(week)+fnameTail
      fp = open(fnameOpen,'r')
      for line in fp:
	line=line.strip().split(',')
	if len(line)==4:  #training dataset
	  inputData=[]
	  outputData=[float(line[2]),float(line[3])]
	  for team in teamlist:	
		if team._id == int(line[0]):
		  inputData.append(team.rypg)
		  inputData.append(team.pypg)
	   	  inputData.append(team.drypg)
		  inputData.append(team.dpypg)
		  print team.name+" vs ",
	  for team in teamlist:	
		if team._id == int(line[1]):
		  inputData.append(team.rypg)
		  inputData.append(team.pypg)
	   	  inputData.append(team.drypg)
		  inputData.append(team.dpypg)
		  print team.name
	  print inputData,outputData
	  dataset.addSample(inputData,outputData)
	  print len(inputData),len(outputData) 
	elif len(line)==2: #task data
	  inputData=[]
	  outputData=[]
	  print "Task data being added in!"
	  for team in teamlist:
		if team._id == int(line[0]):
		  inputData.append(team.rypg)
		  inputData.append(team.pypg)
	   	  inputData.append(team.drypg)
		  inputData.append(team.dpypg)
		  print team.name+" vs ",
	  for team in teamlist:
		if team._id == int(line[1]):
		  inputData.append(team.rypg)
		  inputData.append(team.pypg)
	   	  inputData.append(team.drypg)
		  inputData.append(team.dpypg)
      fp.close()	
  except IOError:
    pass

print "Done loading dataset..."
for data in dataset:
   for a in data:
	print a,
   print "Row: ",
   print data
		  
print " starting NNregression..."
nnr = NNregression(dataset)
nnr.setupNN()
#h=nnr.initGraphics(2,2)
#h.setLineStyle(linewidth=2)
#h.setLegend(['in','out'],loc='upper left')
#from pylab import ion, figure,draw
#print h
#figure()
#ion()
#draw()
##h.show()
nnr.runTraining()
nnr.saveNetwork('savedNetwork.nn')
print "Neural network training completed and saved."

#for team in teamlist:
#	team.printteam()

