import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n)
people=[]
for i in range(n):
    a, b, c = map(int,input().split())
    people.append((a,b,c))
people.sort(key = lambda x: x[0], reverse= True)
# print(people)
dp[0]=people[0][1]
for i in range(n):
    max1=0
    for j in range(0,i):
        if people[i][2]<people[j][2] and dp[j]>max1:
            max1 = dp[j]
    dp[i]=max1+people[i][1]
print(max(dp))
