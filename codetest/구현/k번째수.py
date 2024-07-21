import sys
input = sys.stdin.readline
k=int(input())
for i in range(k):
    n,s,e,k = map(int,input().split())
    num = list(map(int,input().split()))
    num2 = num[s-1:e]
    # print(num2)
    num2.sort()
    # print(num2)
    #print("#"+ str(i+1) +" " +str(num2[k-1]))
    print("#%d %d" %(i+1,num2[k-1]))
