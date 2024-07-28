import sys
input = sys.stdin.readline
a,b = map(int,input().split())
num=[]
for i in str(a):
    num.append(int(i))
# a = list(map(int,str(a)))
# print(num)
stack=[]
for i in num:
    while stack and b>0 and stack[-1]<i:
        stack.pop()
        b-=1
    stack.append(i)
if b!=0:
    stack=stack[:-b]
print(''.join(map(str,stack)))
