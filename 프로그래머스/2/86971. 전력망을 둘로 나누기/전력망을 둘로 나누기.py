def solution(n, wires):
    def DFS(v, visited):
        count = 1
        visited[v] = True
        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                count += DFS(i, visited)
        return count
    
    answer = float(2147000000)
    graph = [[0]*n for _ in range(n)]
    
    for a, b in wires:
        graph[a-1][b-1] = graph[b-1][a-1] = 1

    for a, b in wires:
        graph[a-1][b-1] = graph[b-1][a-1] = 0  # 해당 wire를 끊음
        
        visited = [False] * n
        count1 = DFS(a-1, visited)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))
        
        graph[a-1][b-1] = graph[b-1][a-1] = 1  # wire를 다시 연결
        
    return answer


# from collections import deque
# def bfs(start,visited,graph):
#     queue = deque([start])
#     result = 1
#     visited[start] = True
#     while queue:
#         now = queue.popleft()
#         for i in graph[now]:
#             if visited[i] == False:
#                 result += 1
#                 queue.append(i)
#                 visited[i] = True
                
#     return result
        

# def solution(n, wires):
#     answer = n
#     graph = [[] for _ in range(n+1)]
    
#     for v1,v2 in wires:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#     print(graph)
            
#     for start,not_visit in wires:
#         visited = [False]*(n+1)
#         visited[not_visit] = True
#         result = bfs(start,visited,graph)
#         if abs(result - (n-result)) < answer:
#             answer = abs(result - (n-result))
        
#     return answer
# #no-> bfs 공부하고 다시 풀것

