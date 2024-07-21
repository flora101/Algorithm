import sys
input = sys.stdin.readline
n=int(input())
num = list(map(int,input().split()))

def reverse(x):
    ans=""
    x= str(x)
    for i in range(len(x)):
        ans+=x[len(x)-i-1]
    return int(ans)

def isPrime(x):
    flag=True
    if x ==1:
        flag = False
    for i in range(2,x//2+1):
        if x%i==0:
            flag=False
            break
    return flag
    

for i in num:
    if isPrime(reverse(i))==True:
        print(reverse(i),end=" ")
        
