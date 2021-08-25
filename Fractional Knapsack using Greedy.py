print("enter the objects : ")
O=list(map(str,input().split(" ")))
print("enter the objects' profits : ")
P=list(map(int,input().split(" ")))
print("enter the objects' weights : ")
W=list(map(int,input().split(" ")))
C=int(input("enter the capacity of knapsack : "))
max_profit=0
S=[]
for i in range(0,len(O)):
s = P[i]/W[i]
S.insert(i,s)
def findindex(S):
largest=max(S)
ind=S.index(largest)
return ind
print("-------|-----------|--------------|--------")
print("Object | Weight | Constraints | Profit")
print("-------|-----------|--------------|--------")
while(C>0):
ind=findindex(S)
if W[ind]<=C:
C=C-W[ind]
print(O[ind]+ " | " +str(W[ind])+ " | " +str(C)+ " | " +str(P[ind]))
max_profit += P[ind]
else:
k=C/W[ind]
W[ind]=C
C=C-W[ind]
print(O[ind]+ " | " +str(W[ind])+ " | " +str(C)+ " | " +str(k*P[ind]) )
max_profit += (k*P[ind])
S[ind]=0
print("Maximum profit which can be gained is : ",max_profit)

Best time complexity:O(nlogn)
Average time complexity:O(nlogn)
Worst time complexity:O(nlogn)

Space complexity: O(n)
