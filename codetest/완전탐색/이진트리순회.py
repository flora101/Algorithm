import sys
input=sys.stdin.readline
def DFS(v):#전위순회
    if v>7:
        return
    else:
        print(v,end=" ")
        DFS(v*2)
        DFS(v*2+1)

# def DFS(v): #중위순회
#     if v>7:
#         return
#     else:
#         DFS(v*2)
#         print(v,end=" ")
#         DFS(v*2+1)
        
# def DFS(v): #후위순회
#     if v>7:
#         return
#     else:
#         DFS(v*2)
#         DFS(v*2+1)
#         print(v,end=" ")
        
DFS(1)
