# def solution(distance, rocks, n):
#     answer = []
#     left,right = 0, distance
#     total = len(rocks)-n
#     rocks.sort()
    
#     def check(middle):
#         cnt = 0
#         first = 0
#         for i in rocks:
#             if i-first>=middle:
#                 cnt+=1
#                 first = i
#         return cnt
    
#     while left<=right:
#         mid = (left+right)//2
#         if check(mid)<total:
#             right = mid-1
#         else:
#             answer.append(mid)
#             left=mid+1
#     return max(answer)


def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    
    start = 1 
    end = distance 
    
    while start <= end:
        mid = (start + end) // 2 
        
        previous = 0 
        count = 0
        for rock in rocks:
            if rock - previous < mid:
                count += 1
                if count > n: break 
            else:
                previous = rock
        
        if count > n:
            end = mid - 1 
        else:
            answer = mid 
            start = mid + 1
    
    return answer