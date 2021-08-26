n=4
INF=99999
def floyd_warshall(G):
    A=list(map(lambda i:list(map(lambda j:j,i)),G))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j]=min(A[i][j],A[i][k]+A[k][j])
    print_solution(A)
def print_solution(A):
    for i in range(n):
        for j in range(n):
            if(A[i][j]==INF):
                print("INF",end=" ")
            else:
                print(A[i][j],end=" ")
        print(" ")
G = [[0,5,INF,10],
[INF,0,3,INF],
[INF,INF,0,1],
[INF,INF,INF,0]
]
floyd_warshall(G)

Time complexity:O(n^3)
Space complextity:O(n^2)
