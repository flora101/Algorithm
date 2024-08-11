# def solution(numbers, target):
#     answer = 0
#     ans=[0]
#     for i in numbers:
#         temp=[]
#         for j in ans:
#             temp.append(j+i)
#             temp.append(j-i)
#         ans=temp
#     # print(ans)
#     for i in ans:
#         if i == target:
#             answer+=1
#     return answer
# #no

cnt = 0
def DFS(numbers,target,L,sum1):
    global cnt
    if L==len(numbers):
        if sum1 == target:
            cnt+=1
        return
    DFS(numbers,target,L+1,sum1+numbers[L])
    DFS(numbers,target,L+1,sum1-numbers[L])
    
        
def solution(numbers,target):
    DFS(numbers,target,0,0)
    return cnt
