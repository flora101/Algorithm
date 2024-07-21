import sys
input = sys.stdin.readline
n=int(input())
num =list(map(int,input().split()))
answer=0
sum_num=0
for i in num:
    hap=0
    for j in str(i):
        hap+=int(j)
    if hap>sum_num:
        sum_num = hap
        answer = i
print(answer)
