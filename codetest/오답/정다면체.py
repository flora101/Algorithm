n,m = map(int,input().split())
answer= []
ans = {}
for i in range(1,n+1):
    for j in range(1,m+1):
        if i+j not in ans:
            ans[i+j]=1
        else:
            ans[i+j]+=1
max1 = max(ans.values())
for i in ans:
    if ans[i]==max1:
        answer.append(i)
print(" ".join(map(str,answer)))
