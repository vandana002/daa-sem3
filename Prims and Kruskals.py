//Prims
def prims():
    global vertices,graph,min_weight
    visited=[False]*vertices
    visited[0]=True
    num_edges=0
    while(num_edges<vertices-1):
        min=99999
        x=0
        y=0
        for i in range(vertices):
            if visited[i]:
                for j in range(vertices):
                    if( (not visited[j]) and graph[i][j]):
                        if min>graph[i][j]:
                            min=graph[i][j]
                            x=i
                            y=j

        print(x,"--",y,"-->",graph[x][y])
        min_weight+=graph[x][y]
        visited[y]=True
        num_edges+=1
    
min_weight=0

vertices=int(input('Number of vertices : '))
graph=[list(map(int,input().split())) for i in range(vertices)]
print ("Edges and their weights")
prims()
print('\nMinimum weight : ',min_weight)
 
'''
5
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0

'''
//The time complexity of Prim's algorithm is O(E log V).


//Kruskals
result=[]
sets=[]
v=int(input("Enter no.of vertices")) 
edges={(0,1):5,(1,4):4,(4,3):2,(3,2):3,(2,5):8,(5,0):7,(0,2):3,(1,3):2,(1,2):6}
for i in range(v):
    sets.append([i])
edges=dict(sorted(edges.items(),key=lambda item:item[1]))
def find_set(x):
    for i in range(len(sets)):
            if x in sets[i]:
                return i
for u,v in edges.keys():
    x=find_set(u)
    y=find_set(v)
    if(x!=y):
        result.append((u,v))
        sets[x]+=sets[y] 
        sets.pop(y) 
print("edge : weight")
for i in result:
    print(i,edges[i])

//tc :O(E log E).
