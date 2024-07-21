# import sys
# input = sys.stdin.readline
# n = int(input())
# num = list(map(int,input().split()))
# avg1 = round(sum(num)/n)
# # print(round(avg1))
# min_num = min(num)
# max_num = max(num)
# flag=False
# for i in range(len(num)):
#     if num[i]==avg1:
#         flag = True
#         print(avg1,i+1)
#         break
#     elif num[i]<avg1:
#         min_num = max(min_num,num[i])
#     else:
#         max_num = min(max_num,num[i])
        
# # print(max_num,min_num)
# if flag == False:
#     if abs(max_num)>=abs(min_num):
#         for i in range(len(num)):
#             if num[i]==max_num:
#                 print(avg1, i+1)
#                 break
#     else:
#         for i in range(len(num)):
#             if num[i]==min_num:
#                 print(avg1, i+1)
#                 break



import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx,x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min = tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score = x
            res = idx+1
print(ave,res)
