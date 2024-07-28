import sys
input = sys.stdin.readline
a=input()
ans=''
stack=[]
for i in a:
    if i.isdigit():
        ans+=i
    else:
        if i =="(":
            stack.append(i)
        elif i=="*" or i=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                ans+=stack.pop()
            stack.append(i)
        elif i=="+" or i=="-":
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.append(i)
        elif i==")":
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
while stack:
    ans+=stack.pop()
print(ans)
