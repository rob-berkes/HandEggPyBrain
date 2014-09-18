from lib import team


def buildTeamlist():
  teamlist=[]
  fp = open('teams.csv','r')
  for line in fp:
    line = line.strip().split(',')
    print line
    t = team(line[0],line[1],line[2],line[3],line[4],line[5])
    teamlist.append(t)
  fp.close()
  return teamlist

