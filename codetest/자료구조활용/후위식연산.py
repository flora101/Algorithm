import sys
input = sys.stdin.readline
a=input().rstrip()
stack=[]
ans=0
for i in a:
    if i.isdigit():
        stack.append(int(i))
    else:
        if stack and i == "+":
            v = stack.pop()+stack.pop()
            stack.append(v)
        elif stack and i == "-":
            v = -stack.pop()+stack.pop()
            stack.append(v)
            ans+=v
        elif stack and i =="*":
            v = stack.pop()*stack.pop()
            stack.append(v)
            ans+=v
        elif stack and i =="/":
            v = 1/stack.pop()*stack.pop()
            stack.append(v)
print(v)
