graph = [list(map(int,input().split())) for _ in range(7)]
cnt=0
for i in range(7):
    for j in range(3):
        if graph[i][j:j+5]==graph[i][j:j+5][::-1]:
            cnt+=1
for i in range(7):
    for j in range(3):
        ans=[]
        for k in range(5):
            ans.append(graph[j+k][i])
        if ans==ans[::-1]:
            cnt+=1
print(cnt)
