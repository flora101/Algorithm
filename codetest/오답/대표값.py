n = int(input())
num = list(map(int,input().split()))
avg1 = round(sum(num)/n)
min1 = 2147000000
student = []
for i in range(n):
    min1 = min(min1, abs(num[i]-avg1))
for i in range(n):
    if abs(num[i]-avg1)==min1:
        student.append((num[i],i+1))
student.sort(key = lambda x: x[1])
student.sort(key = lambda x: x[0],reverse=True)
print(avg1, student[0][1])
