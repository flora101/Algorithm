# from collections import deque # deque 선언

# def solution(maps):
#     dx,dy=[-1,1,0,0],[0,0,-1,1]
#     q = deque()
#     a = len(maps)
#     b = len(maps[0])
#     q.append((0,0))
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx= x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<a and 0<=ny<b:
#                 if maps[nx][ny]==1:
#                     maps[nx][ny]=maps[x][y]+1
#                     q.append((nx,ny))
#     if maps[a-1][b-1] != 1: # 만약 1이 아니라면 해당 경우는 가로막히지 않은 경우
#         return maps[a-1][b-1] # 값 리턴
#     else:
#         return -1 # 가로막혀서 접근 불가인 경우 -1 리턴
    
from collections import deque
def solution(maps):
    visited = [[0]*(len(maps[0])) for i in range(len(maps))]
    dis = [[0]*(len(maps[0])) for i in range(len(maps))]
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((0,0))
    visited[0][0]=1
    dis[0][0]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny = y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1 # ==으로 표기
                    dis[nx][ny]=dis[x][y]+1
                    q.append((nx,ny))
    if dis[len(maps)-1][len(maps[0])-1]==0:
        return -1
    else:
        return dis[len(maps)-1][len(maps[0])-1] #-1안해줘씀
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     dx ,dy =  [-1,1,0,0],[0,0,-1,1] #거리 이동을 위한 이동 좌표 설정
#     row = len(maps) # 맵의 크기를 알기위한 변수 설정 1 - 행, 가로
#     col = len(maps[0]) # 맵의 크기를 알기위한 변수 설정 2 - 열, 세로
#     q =  deque()
#     q.append((0,0))
#     while q:  # 해당 while의 경우 q가 빌 때까지
#         x,y = q.popleft() # 들어온 순서대로 가져오기
#         for i in range(4): # 4방위 탐색
#             nx = x + dx[i]
#             ny = y + dy[i] 
#             if 0<= nx < row and 0<= ny < col: # 주어진 맵을 벗어나는지 확인
#                 if maps[nx][ny]==1: # 탐색된 지역이 아닌 경우
#                     maps[nx][ny] = maps[x][y] +1 # 이전 블럭에서 값 +1 해주기
#                     q.append((nx,ny)) # 해당 nx,ny를 deque에 넣어주기
#     if maps[row-1][col-1] != 1: # 만약 1이 아니라면 해당 경우는 가로막히지 않은 경우
#         return maps[row-1][col-1] # 값 리턴
#     else:
#         return -1 # 가로막혀서 접근 불가인 경우 -1 리턴