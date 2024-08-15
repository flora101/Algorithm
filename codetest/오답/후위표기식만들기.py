str1 = input()
stack = []
answer = []
for i in range(len(str1)):
    if str1[i].isdigit():
        answer.append(str1[i])
    else:
        if str1[i]=="(":
            stack.append(str1[i])
        elif str1[i]=="*" or str1[i]=="/":
            while stack and (stack[-1]=="/" or stack[-1]=="*"):
                answer.append(stack.pop())
            stack.append(str1[i])
        elif str1[i]=="-" or str1[i]=="+" :
            while stack and stack[-1]!="(":
                answer.append(stack.pop())
            stack.append(str1[i])
        elif str1[i]==")":
            while stack and stack[-1]!="(":
                answer.append(stack.pop())
            stack.pop()
if len(stack)>0:
    for i in stack:
        answer.append(i)
print("".join(map(str,answer)))
