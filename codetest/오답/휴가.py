n= int(input())
day,money = [],[]
for i in range(n):
    a,b = map(int,input().split())
    day.append(a)
    money.append(b)
day.insert(0,0)
money.insert(0,0)
max_money = -2147000000
def DFS(d,m):
    global max_money
    if d>n+1:
        return
    elif d==n+1:
        if m>max_money:
            max_money = m
    else:
        DFS(d+day[d],m+money[d])
        DFS(d+1,m)
DFS(1,0)
print(max_money)
