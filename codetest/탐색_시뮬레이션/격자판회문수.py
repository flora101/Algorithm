import sys
input=sys.stdin.readline
graph=[list(map(int,input().split())) for _ in range(7)]
def hap(x):
    flag=True
    for i in range(2):
        if x[i]!=x[4-i]:
            flag=False
            break
    return flag
cnt=0
for i in range(7):
    for j in range(3):
        if hap(graph[i][j:j+5]) == True:
            cnt+=1 
for i in range(7):
    for j in range(3):
        col_segment = []
        for k in range(5):
            col_segment.append(graph[j + k][i])
        if hap(col_segment):
            cnt += 1
print(cnt)



# # import sys
# # sys.stdin=open("input.txt", "r")
# # board=[list(map(int, input().split())) for _ in range(7)]
# # cnt=0
# # len=5
# # for i in range(3):
# #     for j in range(7):
# #         tmp=board[j][i:i+len]
# #         if tmp==tmp[::-1]:
# #             cnt+=1
# #         #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
# #         for k in range(len//2):
# #             if board[i+k][j]!=board[len-k+i-1][j]:
# #                 break
# #         else:
# #             cnt+=1
        
# # print(cnt)
