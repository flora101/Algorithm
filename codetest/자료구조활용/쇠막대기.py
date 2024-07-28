import sys
input = sys.stdin.readline
ch=input().rstrip()
stack=[]
cnt=0
for i in range(len(ch)):
    if stack and ch[i-1]=="(" and ch[i] ==")":
        stack.pop()
        cnt+=len(stack)
    elif stack and ch[i-1]==")" and ch[i]==")":
        cnt+=1
        stack.pop()
    else: 
        stack.append(ch[i])
    # print(stack)
print(cnt)
