# import sys
# input = sys.stdin.readline
# graph=[list(map(int,input().split())) for j in range(9)]
# answer=[1,2,3,4,5,6,7,8,9]
# flag=True
# for i in range(9):
#     g1=graph[i].copy()
#     g1.sort()
#     if g1!=answer:
#         flag=False
#         break
# for i in range(9):
#     ans=[]
#     for j in range(9):
#         ans.append(graph[j][i])
#     ans.sort()
#     if ans!=answer:
#         flag=False
#         break
# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         group = []
#         for k in range(3):
#             for l in range(3):
#                 group.append(graph[i + k][j + l])
#         group.sort()
#         if group != answer:
#             flag = False
#             break



import sys
input = sys.stdin.readline
def check(a):
    for i in range(9):#행,열
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
