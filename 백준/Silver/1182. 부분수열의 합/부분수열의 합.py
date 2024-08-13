import sys
from itertools import combinations
input = sys.stdin.readline
n,s= map(int,input().split())
num = list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
    n_list = list(combinations(num,i))
    for x in n_list:
        if sum(x)==s:
            cnt+=1
print(cnt)