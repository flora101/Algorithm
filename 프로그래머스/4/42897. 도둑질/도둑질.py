def solution(money):
    answer = 0
    dp1=[0]*(len(money))
    dp2 = [0]*(len(money))
    dp1[0]=money[0]
    for i in range(1,len(money)-1):
        dp1[i]=max(dp1[i-1],dp1[i-2]+money[i])
    # print(dp1[-2])
    for i in range(1,len(money)):
        dp2[i]=max(dp2[i-1],dp2[i-2]+money[i])
    # print(dp2[-1])
    return max(dp1[-2],dp2[-1])