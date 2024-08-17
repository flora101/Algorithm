# from itertools import permutations
# answer = 0
# def dfs(k,cnt,dungeons,visited):
#     global answer
#     if cnt>answer:
#         answer = cnt
#     for i in range(len(dungeons)):
#         if not visited[i] and k>= dungeons[i][0]:
#             visited[i]=True
#             dfs(k-dungeons[i][1],cnt+1,dungeons,visited)
#             visited[i]=False
# def solution(k, dungeons):
#     global answer
#     visited = [False] * len(dungeons)
#     dfs(k,0,dungeons,visited)
#     return answer



from itertools import permutations
def solution(k, dungeons):
    d = len(dungeons)
    per = list(permutations(range(d)))
    max1=-2147000000
    # print(per)
    def DFS(k,tu):
        cnt=0
        for i in range(len(tu)):
            # print(k,tu)
            if k>=dungeons[tu[i]][0]:
                k-=dungeons[tu[i]][1]
                cnt+=1
            else:
                break
        return cnt
    for i in per:
        max1 =max(max1,DFS(k,i))
    return max1












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # answer = -1
    # for i in permutations(dungeons,len(dungeons)):
    #     print(i)
    #     now = k
    #     cnt = 0
    #     for need,use in i:
    #         if now>=need:
    #             now-=use
    #             cnt+=1
    #     answer=max(answer,cnt)
    # return answer
#no 순열