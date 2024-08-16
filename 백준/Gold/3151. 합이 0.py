import sys
input= sys.stdin.readline
n=int(input())
student = list(map(int,input().split()))
team = 0
student.sort()
# print(student)
def help(left,right,v):
    global team
    end = n
    while left<right:
        tmp = student[left]+student[right]
        if tmp<v:
            left+=1
        elif tmp>v:
            right-=1
        else:
            if student[left] == student[right]: # [-4 2 2 2]
                team+=(right-left)
            else: # [-5 0 5 5 5]
                if end>right:
                    end = right # right에서1씩 줄이면서 arr[right]와 같은게 몇갠지 찾기
                    while end>=0 and student[end-1]==student[right]:
                        end-=1
                team+=(right-end+1)
            left+=1
            
for i in range(n-2):
    goal= -student[i]
    left,right = i+1,n-1
    help(left,right,goal)
    
print(team)
