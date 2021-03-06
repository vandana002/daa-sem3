#Matrix chain multiplication - DP

def printbest(b, i, j):
    if i==j:
        print("A",i,end=" ")
    else:
        print('(',end="")
        printbest(b, i, b[i][j])
        printbest(b, b[i][j] + 1, j)
        print(')',end="")
        
n=4
print("no.of matrices is ",n)
print("enter dimensions")
d=[]
for i in range(0,n+1):
    d.append(int(input()))

n+=1
m=[]
b=[]

#d=[5,4,6,2,7]
m=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
b=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for L in range(2,n):
    for i in range(1,n-L+1):
        j=i+L-1
        m[i][j]=999999
        for k in range(i,j):
            cost=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
            if(cost<m[i][j]):
                m[i][j]=cost
                b[i][j]=k
            print(cost)
print("the minimum no.of multiplications are ",m[1][n-1])
print("and the order is ")
printbest(b,1,n-1)


Time complexitity:O(n^3) where extra spaces take O(n^2)
