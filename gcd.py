def gcd(a,b):
    if(b==0):
        return a 
    return gcd(b,a%b)
a=int(input())
b=int(input())
if(gcd(a,b)):
    print('Gcd of',a,'and',b,'is',gcd(a,b))
else:
    print("not found")
    
time complexity:O(log n)
