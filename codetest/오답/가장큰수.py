a,b=map(int,input().split())
num=[]
for i in str(a):
    num.append(int(i))
stack =[]
for i in range(len(num)):
    while stack and stack[-1]<num[i] and b>0:
        stack.pop()
        b-=1
    stack.append(num[i])
if b!=0:
    stack = stack[:b]
print(''.join(map(str,stack)))
