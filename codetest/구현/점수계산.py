import sys
input = sys.stdin.readline
n=int(input())
num = list(map(int,input().split()))
total=0
score=0
for i in range(n):
    if num[i]==1:
        score+=1
        total+=score
    elif num[i]==0:
        score=0
    # print(score)
print(total)
