// first pivot

def partition(list,start,end):
pivot=list[start]
x=start+1
y=end
global com
while True:
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
list[start],list[y]=list[y],list[start]
return y

def quickSort(list,start,end):
if start<end:
z=partition(list,start,end)
quickSort(list,start,z-1)
quickSort(list,z+1,end)
timeList=[]
comList=[]
for i in range(200):
com=1
arr=[]
for j in range(0,i):
n = random.randint(1,100)
arr.append(n)
start = timeit.default_timer()
quickSort(arr,0,i-1)
end = timeit.default_timer()
total=end-start
timeList.append(total)
comList.append(com)

timeList = [x * 1000 for x in timeList]
n = [*range(1, 201, 1)]
nn=[]
for x in n:

nn.append(math.pow(x,2))

nnn=[]
for x in n:

nnn.append(x*math.log(x,2))

plt.plot(comList,n,color='yellow', linewidth=3,label='Quicksort time')
plt.plot(nn,n,color='red', linewidth=3,label='n^2')
plt.plot(nnn,n,color='blue', linewidth=3,label='nlogn')
plt.title('Quick Sort Running time')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()