import sys
from itertools import permutations, combinations
input = sys.stdin.readline
n,k = map(int,input().split())
num = list(map(int,input().split()))
num2 = set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            num2.add(num[i]+num[j]+num[m])
num2 = list(num2)
num2.sort(reverse=True)
print(num2[k-1])
