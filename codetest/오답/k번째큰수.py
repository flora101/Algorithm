n,m = map(int,input().split())
num = list(map(int,input().split()))
answer = set()
for i in range(n):
    ans=0
    for j in range(i+1,n):
        for k in range(j+1,n):
            ans= num[i]+num[j]+num[k]
            answer.add(ans)
answer = list(answer)
answer.sort(reverse=True)
print(answer[m-1])
