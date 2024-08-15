# def solution(distance, rocks, n):
#     answer = []
#     left,right = 1, distance
#     rocks.append(distance)
#     rocks.sort()
    
#     while left<=right:
#         mid = (left+right)//2
#         cnt = 0
#         first = 0
#         for i in rocks:
#             if i-first<mid:
#                 cnt+=1
#             else:
#                 first = i
#             if cnt>n:
#                 break
#         if cnt>n:
#             right = mid-1
#         else:
#             answer.append(mid)
#             left=mid+1
#     return max(answer)


def solution(distance, rocks, n):
    answer = []
    left,right = 0, distance
    total = len(rocks)-n+1
    rocks.append(distance)
    rocks.sort()
    
    def check(middle):
        cnt = 0
        first = 0
        for i in rocks:
            if i-first>=middle:
                cnt+=1
                first = i
        return cnt
    
    while left<=right:
        mid = (left+right)//2
        if check(mid)<total:
            right = mid-1
        else:
            answer.append(mid)
            left=mid+1
    return max(answer)
