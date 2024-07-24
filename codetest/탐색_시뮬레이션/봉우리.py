import sys
input = sys.stdin.readline
n=int(input())
board=[[0 for j in range(n+2)] for i in range(n+2)]
card = [list(map(int,input().split())) for i in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
for i in range(n):
    for j in range(n):
        board[i+1][j+1]=card[i][j]
# print(board)
for i in range(1,n+2):
    for j in range(1,n+2):
        flag=True
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if board[i][j]<=board[nx][ny]:
                flag=False
                break
        if flag==True:
            cnt+=1
print(cnt)
