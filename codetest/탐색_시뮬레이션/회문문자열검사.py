import sys
input = sys.stdin.readline
n=int(input())
for i in range(n):
    voc = input().rstrip()
    voc = voc.upper()
    # v=len(voc)
    # flag=True
    # for j in range(v//2):
    #     if voc[j]!=voc[v-1-j]:
    #         flag=False
    #         break
    # if flag == True:
    #     print("#%d YES" %(i+1))
    # else:
    #     print("#%d NO" %(i+1))
    if voc==voc[::1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
