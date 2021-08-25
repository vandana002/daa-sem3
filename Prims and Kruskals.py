//Prims
INF = 9999999
V = 5
G = [[0, 9, 75, 0, 0],
[9, 0, 95, 19, 42],
[75, 95, 0, 51, 66],
[0, 19, 51, 0, 31],
[0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True
print("Edge : Weight\n")
while (no_edge < V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" +
    str(G[x][y])) 
    selected[y] = True
    no_edge += 1
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
