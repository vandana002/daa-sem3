A=[[1,2,3],
[5,6,7],
[8,9,7]]
B=[[5,6,8],
[8,9,7],
[3,5,1]]
result=[[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][j]*B[k][j]
for r in result:
    print(r)
    
Tc: O(n^3)
  Sc: O(n^3)
