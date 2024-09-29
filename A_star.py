from heapq import heapify,heappop,heappush
from collections import defaultdict
import numpy as np
import random 
import matplotlib.pyplot as plt
import math
rows=20
cols=30
map = np.random.rand(rows, cols)<0.1
print(map)
start  =(0,0)
goal  =(18,28)
def get_neighbour(u):
    neighbour = []
    disp = ((0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1))  # possible movement
    if u==(0,15):   ## introduced A worm hole
        return([(0,(15,15))])
    for delta in disp:
        cand  =(u[0]+delta[0],u[1]+delta[1])
        if cand[0]>=0 and cand[0]<len(map) and cand[1]>=0 and cand[1]<len(map[0]) and map[cand[0]][cand[1]]==False:
            neighbour.append((math.sqrt(delta[0]**2+delta[1]**2),cand))
    return(neighbour)




plt.imshow(map) # shows the map
plt.ion() # turns 'interactive mode' on
plt.plot(goal[1],goal[0],'y*') # puts a yellow asterisk at the goal
queue = [(0,start)]
heapify(queue)
distances=defaultdict(lambda:float("inf"))
distances[start] = 0
visited={start}
parent = {}
while queue:
    (currDist,v) = heappop(queue)
    if v == goal:
        break
    #print(v)    
    plt.plot(v[1],v[0],'g*')    
    plt.show()
    plt.pause(0.000001) 
    visited.add(v)
    for (costvu,u) in get_neighbour(v):
        if u not in visited:
            newCost = distances[v] + costvu 
            if newCost<distances[u]:
                distances[u] = newCost
                heappush(queue,(newCost + np.sqrt((goal[0]-u[0])**2+(goal[1]-u[1])**2),u))
                parent[u]=v

key = goal
path =[]
while key in parent.keys():
    key = parent[key]
    path.insert(0,key)
path.append(goal)
print(path)

for p in path:    
     plt.plot(p[1],p[0],'r.')

plt.ioff()
plt.show()    


