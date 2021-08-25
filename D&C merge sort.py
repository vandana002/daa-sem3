import random
import timeit
import matplotlib.pyplot as plt
import math
#####################################
def mergeSort(A):
if len(A)>1:
mid=int(len(A)/2)
L=A[:mid] #dividing array into two halves
R=A[mid:]
#print(L)
#print(R)
mergeSort(L)
mergeSort(R)
mergePro(A,L,R)

#####################################
def mergePro(A,L,R):
i = j = k = 0
while i < len(L) and j < len(R):
global com
if L[i] < R[j]:
com=com+1
A[k] = L[i]
i += 1
else:
com=com+1
A[k] = R[j]
j += 1
k += 1
# Checking if any element was left
while i < len(L):
A[k] = L[i]
i += 1
k += 1
while j < len(R):
A[k] = R[j]
j += 1
k += 1

#####################################
timeList=[]
comList=[]
for p in range(200):
com=1 #no of comparision to sort
#print(p)
A = []
for i in range(0,p):
n = random.randint(1,100)

A.append(n)
# starting time
#start = timeit.default_timer()
mergeSort(A);
# end time
#end = timeit.default_timer()
# total time taken
#total=end-start
#timeList.append(total)
comList.append(com)
#timeList = [x * 1000 for x in timeList]
n = [*range(1, 201, 1)]
#nn=[x*(math.log(x,2)) for x in n]
nn=[]
for x in n:

nn.append(x*math.log(x,2))

#print(nn)
#print(comList)
#comList=[(math.log(x,2)) for x in comList]
#print(comList)
plt.plot(comList,n,color='green', linewidth=3,label='Mergesort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.title('Merge Sort Running ime')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()
