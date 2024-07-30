import sys
input=sys.stdin.readline
n=int(input())
# a=[]
# def DFS(x):
#     if x>=1:
#         a.append(x%2)
#         x=x//2
#         DFS(x)
# DFS(n)
# a=a[::-1]
# print(''.join(map(str,a)))

def DFS(x):
    if x==0:
        return #그냥 종료
    else:
        DFS(x//2)
        print(x%2,end='')
DFS(n)
