class team:
    _id = 0
    name = 'full team name'
    pypg = 0.0
    rypg = 0.0
    dpypg = 0.0
    drypg = 0.0

    def __init__(self,_id,name,rypg,pypg,drypg,dpypg):
	self._id = int(_id)
	self.name = name
	self.pypg = 1/(float(pypg))
	self.rypg = 1/(float(rypg))
	self.drypg = 1/(float(drypg))
	self.dpypg = 1/float(dpypg)

    def printteam(self):
	print "================Team Report==========="
	print self.name
	print "Id number: " +str(self._id)
	print 'Passing Yards per game: '+ str(self.pypg)
	print 'Rushing Yards per game: '+ str(self.rypg)
        print 'Defense Passing: '+str(self.dpypg)
	print 'Defense Rushing: '+str(self.drypg)

    def printdataset(self):
	print self.name+"  Id number: " +str(self._id)
	print "("+str(round(self.pypg,5))+","+str(round(self.rypg,5))+ \
		","+str(round(self.dpypg,5))+","+str(round(self.drypg,5))+")"

    def printteam(self):
	print "Id number: "+str(self._id)+"  "+self.name	
