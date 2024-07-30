# import sys
# input = sys.stdin.readline
# n=int(input())
# a=list(map(int,input().split()))
# total=sum(a)
# def DFS(l,sum):
#     if sum>total//2:
#         return
#     if l==n:
#         if sum==(total-sum):
#             print("YES")
#             sys.exit(0)#함수만 종료가 아니라 프로그램이 다 종료!
#     else:
#         DFS(l+1,sum+a[l])
#         DFS(l+1,sum)

# DFS(0,0)
# print("NO")

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
found = False

def DFS(l, sum):
    global found
    if sum > total // 2:
        return
    if l == n:
        if sum == (total - sum):
            found = True
        return
    else:
        DFS(l + 1, sum + a[l])
        DFS(l + 1, sum)

DFS(0, 0)

if found:
    print("YES")
else:
    print("NO")
