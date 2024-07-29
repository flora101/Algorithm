import sys
input=sys.stdin.readline
voc1=input().rstrip()
voc2=input().rstrip()
vo1={}
vo2={}
for i in voc1:
    if i not in vo1:
        vo1[i]=1
    else:
        vo1[i]+=1
# print(vo1)
for i in voc2:
    if i not in vo2:
        vo2[i]=1
    else:
        vo2[i]+=1
if vo1==vo2:
    print("YES")
else:
    print("NO")
