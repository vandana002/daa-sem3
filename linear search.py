lst = []
num = int(input("Enter size of list :- "))
for n in range(num):
    numbers = int(input("Enter the array of %d element :- " %n))
    lst.append(numbers)
x = int(input("Enter number to search in list :- "))
i = 0
flag = False
for i in range(len(lst)):
    if lst[i] == x:
        flag = True
        break
if flag == 1:
    print('{} was found at index {}.'.format(x, i))
else:
    print('{} was not found.'.format(x))

Time complexity of LINEAR SEARCH algorithm -
Base Case - O(1)
Average Case - O(n)
Worst Case -O(n)
