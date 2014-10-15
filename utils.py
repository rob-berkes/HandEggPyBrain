from lib import team
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.neuralnets import NNregression
from lib import team
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader


def buildRecurrentNetwork():
   nn=buildNetwork(8,5,2,recurrent=True)
   return nn
def loadRecurrentNetwork(fname):
  nn=NetworkReader.readFrom(fname)
  return nn  
def buildTeamlist():
  teamlist=[]
  fp = open('data/teams.csv','r')
  for line in fp:
    line = line.strip().split(',')
    print line
    t = team.team(line[0],line[1],line[2],line[3],line[4],line[5])
    teamlist.append(t)
  fp.close()
  return teamlist
def updateDataset():
  teamlist=buildTeamlist()
  dataset=SupervisedDataSet(8,2)
  fnameOpen='data/update.csv'
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
  fp.close()	
  return dataset
def buildDataset():
  teamlist=buildTeamlist()
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
  return dataset

