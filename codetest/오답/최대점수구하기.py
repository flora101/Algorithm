n,m = map(int,input().split())
score=[]
time=[]
for i in range(n):
    a,b = map(int,input().split())
    score.append(a)
    time.append(b)
max_score=-2147000000
def DFS(L,s,t):
    global max_score
    if t>m:
        return
    if L==n:
        if s>max_score:
            max_score=s
    else:
        DFS(L+1,s+score[L],t+time[L])
        DFS(L+1,s,t)
DFS(0,0,0)
print(max_score)
