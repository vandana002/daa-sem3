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
while (no_edge < V - 1):.
minimum = INF
x = 0
y = 0
for i in range(V):
if selected[i]:
for j in range(V):
if ((not selected[j]) and G[i][j]):
# not in selected and there is an edge
if minimum > G[i][j]:
minimum = G[i][j]
x = i
y = j

print(str(x) + "-" + str(y) + ":" +
str(G[x][y])) selected[y] = True
no_edge += 1

//The time complexity of Prim's algorithm is O(E log V).


//Kruskals
class Graph:
def __init__(self, vertices):
self.V = vertices
self.graph = []
def add_edge(self, u, v, w):
self.graph.append([u, v, w])
def find(self, parent, i):
if parent[i] == i:
return i
return self.find(parent, parent[i])
def apply_union(self, parent, rank, x,
y): xroot = self.find(parent, x)
yroot = self.find(parent, y)
if rank[xroot] < rank[yroot]:
parent[xroot] = yroot
elif rank[xroot] > rank[yroot]:
parent[yroot] = xroot
else:
parent[yroot] = xroot
rank[xroot] += 1
def kruskal_algo(self):
result = []
i, e = 0, 0
self.graph = sorted(self.graph, key=lambda item:
item[2]) parent = []
rank = []
for node in range(self.V):
parent.append(node)

rank.append(0)
while e < self.V - 1:
u, v, w = self.graph[i]
i = i + 1
x = self.find(parent, u)
y = self.find(parent, v)
if x != y:
e = e + 1
result.append([u, v, w])
self.apply_union(parent, rank, x, y)
for u, v, weight in result:
print("%d - %d: %d" % (u, v, weight))

g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()

//tc :O(E log E).
