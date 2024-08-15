def solution(n, times):
    answer = []
    left,right=1,max(times)*n
    while left<=right:
        mid = (left+right)//2
        person = 0
        for i in times:
            person += (mid//i)
        if person>=n:
            answer.append(mid)
            right = mid-1
        else:
            left=mid+1
    return min(answer)