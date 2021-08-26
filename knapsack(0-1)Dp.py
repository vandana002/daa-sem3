val=input("enter the values:")
val=val.split()
for i in range(len(val)):
    val[i]=int(val[i])
wt=input("enter the weights:")
wt=wt.split()
for i in range(len(wt)):
    wt[i]=int(wt[i])
W=int(input("enter the capacity:"))
n=len(val)
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
for i in range(n+1):
    for w in range (W+1):
        if i==0 or w ==0:
            K[i][w]=0
        elif wt[i-1] <= w:
            K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
        else:
            K[i][w] = K[i-1][w]
a= len(K)
pft = max(K[a-1])
max_profit = pft
while(a>-1):
    if pft in K[a-2]:
        a=a-1
        continue
    else:
        print("items that are contributed are:{}".format(a))
        pft=pft-val[a-2]
        a=a-1
print('The maximum profit of items {}:'.format(max_profit))

Time complexity: O(nW)
Space complexity: O(nW)

