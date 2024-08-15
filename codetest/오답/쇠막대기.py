# str1 = "()(((()())(())()))(())"
str1 = input()
answer=0
stack =[]
for i in range(len(str1)):
    if str1[i] =="(":
        stack.append(i)
    else:
        if str1[i-1]=="(":
            stack.pop()
            answer+=len(stack)
        else:
            stack.pop()
            answer+=1
print(answer)
