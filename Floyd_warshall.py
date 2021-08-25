no_of_vertices = 4
INF = 999
def floyd_warshall(G):
distance = list(map(lambda i: list(map(lambda j: j, i)), G))

for k in range(no_of_vertices):
for i in range(no_of_vertices):
for j in range(no_of_vertices):
distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
print_solution(distance)

# Printing the solution
def print_solution(distance):
for i in range(no_of_vertices):
for j in range(no_of_vertices):
if(distance[i][j] == INF):
print("INF", end=" ")
else:
print(distance[i][j], end=" ")
print(" ")

G = [[0,5,INF,10],
[INF,0,3,INF],
[INF,INF,0,1],
[INF,INF,INF,0]
]
floyd_warshall(G)

Time complexity:O(n^3)
Space complextity:O(n^2)
