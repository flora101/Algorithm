n = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True)
price = int(input())
min_coin = 2147000000
def DFS(count, sum1):
    global min_coin
    if count>min_coin:
        return 
    if sum1 == price:
        min_coin = min(min_coin,count)
        return min_coin
    elif sum1> price:
        return 
    else:
        for i in coin:
            DFS(count+1,sum1+i)
DFS(0,0)
print(min_coin)
