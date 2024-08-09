# # 내가 푼 풀이!! # Bottom-up 방식
# import sys
# input = sys.stdin.readline
# n = int(input())
# graph = [list(map(int,input().split())) for i in range(n)]
# dp = [[0]*(n) for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==0 and j ==0:
#             dp[i][j]=graph[i][j]
#         if i == 0:
#             dp[i][j] = dp[i][j-1]+ graph[i][j]
#         if j == 0:
#             dp[i][j] = dp[i-1][j]+graph[i][j]
# for i in range(1,n):
#     for j in range(1,n):
#         dp[i][j] = graph[i][j] + min(dp[i][j-1],dp[i-1][j])
# print(dp[n-1][n-1])



# Top-Down 방식 DP (재귀 방식)
import sys
input = sys.stdin.readline
def DFS(x,y):
    if dy[x][y]>0: # 메모리제이션+ cutedge해줘야지 time limit안남
        return dy[x][y]
    if x ==0 and y==0:
        return arr[0][0]
    else: 
        if y == 0:
            dy[x][y] = DFS(x-1,y)+arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x,y-1)+arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + arr[x][y]
        return dy[x][y]
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*(n) for _ in range(n)] # 메모리제이션 하기위해
print(DFS(n-1,n-1))
