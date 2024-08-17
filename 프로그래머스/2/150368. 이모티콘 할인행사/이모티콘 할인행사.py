from itertools import product
def solution(users, emoticons):
    answer = [0,0]
    data = [10,20,30,40]
    # discount=[]
    discount= list(product(data,repeat=len(emoticons)))
    # print(em_dis)
    for d in range(len(discount)):
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                # 할인율을 만족하면 구매
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100
        
        # 구매 금액에 따라 가입자 갱신
        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0
        
        # 최대 가입자, 구매 금액 갱신
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join
    
    return answer