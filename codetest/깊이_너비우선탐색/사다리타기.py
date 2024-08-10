# import sys
# input = sys.stdin.readline
# graph = [list(map(int,input().split())) for _ in range(10)]
# ch = [[0]*10 for _ in range(10)]
# dx= [-1,1, 0]
# dy = [0,0,1]
# for i in range(10):
#     for j in range(10):
#         if graph[i][j] == 2:
#             des = (i,j)
# # print(des)
# start = []
# for i in range(10):
#     if graph[0][i]==1:
#         start.append(i)
# # print(start)
# def DFS(start_x,start_y):
#     ch[start_x][start_y]=1
#     if start_x == 9:
#         return start_y
#     else:
#         for i in range(3):
#             nx = start_x + dx[i]
#             ny = start_y + dy[i]
#             if 0<=nx<10 and 0<=ny<10:
#                 if graph[nx][ny]==1 and ch[nx][ny]==0:
#                     ch[nx][ny]=1
#                     # print(nx,ny)
#                     DFS(nx,ny)

# for i in range(len(start)):
#     x = 0
#     y = start[i]
#     if DFS(x,y) == des[1]:
#         print(y)
    
    
# => 내 풀인데 왜 틀린지 모르겠다....
    
import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
def DFS(x,y):
    ch[x][y]=1
    if x ==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1] == 1 and ch[x][y-1]==0:
            DFS(x,y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        else:
            DFS(x-1, y)

for y in range(10):
    if board[9][y]==2:
        DFS(9,y)
