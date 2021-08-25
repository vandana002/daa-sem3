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
    for j in range(len(A[0])):
            result[i][j]+=A[i][j]*B[i][j]
for r in result:
    print(r)
 
 
 Tc: O(n^2)
 Sc: O(n^2)
