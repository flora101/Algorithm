import sys
input = sys.stdin.readline
card = [i+1 for i in range(20)]
for i in range(10):
    ai,bi = map(int,input().split())
    card=card[:ai-1]+card[ai-1:bi][::-1]+card[bi:]
print(' '.join(map(str,card)))
    
    
# a = list(range(21))
# for _ in range(10):
#     ai,bi = map(int,input().split())
#     for i in range((bi-ai+1)//2):
#         a[ai+i],a[bi-i]=a[bi-i],a[ai+i]
# a.pop(0)
# for x in a:
#     print(x,end=" ")
