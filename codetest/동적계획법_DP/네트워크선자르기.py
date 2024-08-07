# Bottom up 방법
# import sys
# input = sys.stdin.readline
# n=int(input())
# dy = [0]*(n+1)
# dy[1]=1
# dy[2]=2
# for i in range(3,n+1):
#     dy[i]=dy[i-1]+dy[i-2]
# print(dy[n])


# Top down 방법(미리 한번 구한걸 메모해놓고 불필요한 재귀 호출 막기)
import sys
input = sys.stdin.readline
n=int(input())
dy=[0]*(n+1)
def DFS(len1):
    if dy[len1]>0: #값이 있는거(가치컷= 메모리제이션)
        return dy[len1]
    if len1 == 1 or len1 ==2:
        return len1
    else:
        dy[len1]=DFS(len1-1)+DFS(len1-2)
        return dy[len1]
print(DFS(n))
