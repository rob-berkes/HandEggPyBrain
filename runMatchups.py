#load trained network and run matchups. 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkreader import NetworkReader
from utils import buildTeamlist

teamlist = buildTeamlist()
nn=buildNetwork(8,5,2)
nn=NetworkReader.readFrom('recurrentNetwork.xml')
#nn=NetworkReader.readFrom('savedNetwork.nn')

print "loaded Network, now running matchups..."
fp =open('data/matchups.csv','r')
for line in fp:
  attList=[]
  line = line.strip().split(',')
  for team in teamlist:
    if int(team._id) == int(line[0]):
      print team.name,
      attList.append(team.rypg)
      attList.append(team.pypg)
      attList.append(team.drypg)
      attList.append(team.dpypg)
  for team in teamlist:
    if int(team._id) == int(line[1]):
      print " vs. "+team.name
      attList.append(team.rypg)
      attList.append(team.pypg)
      attList.append(team.drypg)
      attList.append(team.dpypg)
  print nn.activate(attList)


