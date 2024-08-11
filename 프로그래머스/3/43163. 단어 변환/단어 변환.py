from collections import deque
def bfs(begin,target,words):
    q=deque()
    q.append([begin,0])
    while q:
        b,L = q.popleft()
        if b == target:
            return L
        else:
            for i in words:
                cnt=0
                for j in range(len(i)):
                    if b[j]!=i[j]:
                        cnt+=1
                if cnt ==1:
                    q.append((i,L+1))
                        
def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin,target,words)