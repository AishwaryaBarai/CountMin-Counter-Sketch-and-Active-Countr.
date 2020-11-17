import random
import sys

k = 3
w = 3000
numFlows = 0

hashes=random.sample(range(0, sys.maxsize), k)

counters=[[0 for _ in range(w)] for __ in range(k)]

f = open("project3input.txt","r")

sys.stdout  =  open("CountMinPython.txt","w")


flag = True

ipMap = []
randomValSet = set()
ips = {}
for line in f:
  if flag == True:
    numFlows = int(line)
    flag = False
  else:
    line = line.split()
    if line[0] not in ips:
      someRandom = random.randint(0, sys.maxsize)
      while (someRandom in randomValSet):
        someRandom = random.randint(0, sys.maxsize)
      ips[line[0]] = someRandom
      ipMap.append([line[0], someRandom, int(line[1])])
    else:
      someRandom = ips[line[0]]
    for c in range(k):
      location = (someRandom ^ hashes[c]) % w
      counters[c][location] += int(line[1])


error = 0
for ip in ipMap:
  expected = 100000000
  for c in range(k):
    location = (ip[1] ^ hashes[c]) % w
    expected=min(expected,counters[c][location])
  error += expected - ip[2]
  ip.append(expected)
  
  

print(int(error / len(ipMap)) )
ipMap.sort(key = lambda x: -x[3])
for i in range(100):
  print(ipMap[i][0], ipMap[i][3], ipMap[i][2])

sys.stdout.close()