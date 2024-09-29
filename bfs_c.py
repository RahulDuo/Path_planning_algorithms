import numpy as np
import random 
import matplotlib.pyplot as plt
rows=20
cols=30
map = np.random.rand(rows, cols)<0.1
print(map)

graph = {
    'A':['B','C']
    ,'B':['A','D','E']
    ,'C':['A','F']
    ,'D':['B']
    ,'E':['B','F']
    ,'F':['C','E']
}
#map = [[0,0,0],[0.9,0.8,0],[0,0,0]]
def get_neighbour(u):
    neighbour = []
    disp = ((0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1))  # possible movement
    for delta in disp:
        cand  =(u[0]+delta[0],u[1]+delta[1])
        if cand[0]>=0 and cand[0]<len(map) and cand[1]>=0 and cand[1]<len(map[0]) and map[cand[0]][cand[1]]==False:
            neighbour.append(cand)
    return(neighbour)
start= (0,0)
goal = (15,2)
plt.imshow(map) # shows the map
plt.ion() # turns 'interactive mode' on
plt.plot(goal[1],goal[0],'y*') # puts a yellow asterisk at the goal
queue = [start]
visited = {start} # set because :look up is O(1) operation
# Set is a hash data structure
parent = {}
while queue:

    v = queue.pop(0)  
    if v == goal:
        break
    #print(v)    
    plt.plot(v[1],v[0],'g*')    
    plt.show()
    plt.pause(0.000001) 
    
    for u in get_neighbour(v):
        
        if u not in visited:
            queue.append(u)
            visited.add(u)
            parent[u]=v
key =goal
path=[]
while key in parent.keys():
    key = parent[key]
    path.insert(0,key)
path.append(goal)

print(path)




for p in path:    
     plt.plot(p[1],p[0],'r.')

plt.ioff()
plt.show()    




