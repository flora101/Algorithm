n = int(input())
num1= list(map(int,input().split()))
m=int(input())
num2= list(map(int,input().split()))
s1,s2 = 0,0
answer=[]
while 1:
    if s1>=n:
        for i in num2[s2:]:
            answer.append(i)
        break
    elif s2>=m:
        for i in num1[s1:]:
            answer.append(i)
        break
    else:
        if num1[s1]<=num2[s2]:
            answer.append(num1[s1])
            s1+=1
        else:
            answer.append(num2[s2])
            s2+=1
print(" ".join(map(str,answer)))
