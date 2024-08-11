# 내가 푼 풀이 틀림..
# def DFS(tic_len1, L, graph1, start1, answer1):
#     if L == tic_len1:
#         return answer1
#     else:
#         for i in range(len(graph1)):
#             if graph1[start1][i]==1:
#                 graph1[start1][i]=0
#                 answer1.append(i)
#                 DFS(tic_len1,L+1,graph1,i,answer1)
                
        
# def solution(tickets):
#     tic_len = len(tickets)
#     airport = []
#     air_dic = {}
#     air_dic_re = {}
#     for i in tickets:
#         if i[0] not in airport:
#             airport.append(i[0])
#         if i[1] not in airport:
#             airport.append(i[1])
#     airport.sort()
#     for i in range(len(airport)):
#         air_dic[airport[i]]=i
#         air_dic_re[i]=airport[i]
#     # print(air_dic)
#     # print(air_dic_re)
#     graph = [[0]*(len(airport)) for i in range(len(airport))]
#     visited = [[0]*(len(airport)) for i in range(len(airport))]
#     for i in tickets:
#         graph[air_dic[i[0]]][air_dic[i[1]]]=1
#     # print(graph)
#     star = air_dic['ICN']
#     answer=[star]
#     DFS(tic_len, 0, graph, star, answer)
#     very=[]
#     for i in answer:
#         very.append(air_dic_re[i])
#     return very

def solution(tickets):
    answer= []
    visited= [0]*(len(tickets))
    def DFS(start,path):
        if len(path)==len(tickets)+1:
            answer.append(path)
            return
        else:
            for idx,ticket in enumerate(tickets):
                if ticket[0]==start and visited[idx]==0:
                    visited[idx]=1
                    DFS(ticket[1],path+[ticket[1]])
                    visited[idx]=0
    DFS("ICN",["ICN"])
    answer.sort()
    return answer[0]