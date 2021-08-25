import random
import timeit
import matplotlib.pyplot as plt
import math
def partition(list,start,end):
pivot=list[end]
x=start
y=end-1
global com
while(1):
while x<=y and list[x]<=pivot:
x+=1
com+=1
while x<=y and list[y]>=pivot:
y-=1
com+=1
if(x<y):
list[x],list[y]=list[y],list[x]
com+=1
else:
com+=1
break
list[end],list[x]=list[x],list[end]

return x
def partition_rand(list,start,end):
randpivot = random.randrange(start,end)
list[end],list[randpivot]=list[randpivot],list[end]
return partition(list,start,end)
def quickSort(list,start,end):
if start<end:
z=partition_rand(list,start,end)
quickSort(list,start,z-1)
quickSort(list,z+1,end)
#------------------------------
timeList=[]
comList=[]
for i in range(200):
com=1
arr=[]
for j in range(0,i):
n = random.randint(1,100)
list.append(n)
start = timeit.default_timer()
quickSort(arr,0,i-1)
end = timeit.default_timer()
#print(arr)
total=end-start
timeList.append(total)
comList.append(com)
timeList = [x * 1000 for x in timeList]
avgtime=0
for i in timeList:
avgtime+=i
avgtime/=200
n = [*range(1, 201, 1)]
nn=[]
for x in n:

nn.append(math.pow(x,2))

nnn=[]
for x in n:

nnn.append(x*math.log(x,2))

print("Time required = ",avgtime)
plt.plot(comList,n,color='yellow', linewidth=3,label='Quicksort time')
plt.plot(nn,n,color='red', linewidth=3,label='n^2')
plt.plot(nnn,n,color='blue', linewidth=3,label='nlogn')
plt.title('Quick Sort Running time')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()


The best and average complexities are O(nlogn) and for the worst case it is n^2.
