def solution(word):
    answer = 0
    alp = ['A','E','I','O','U']
    res = []
    def DFS(v,w):
        if v == 5:
            return
        else:
            for i in range(5):
                res.append(w+alp[i])
                DFS(v+1,w+alp[i])
    DFS(0,"")
    # print(res)
    return res.index(word)+1
