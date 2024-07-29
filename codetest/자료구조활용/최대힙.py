from queue import PriorityQueue
import sys
input = sys.stdin.readline
pq=PriorityQueue()
while 1:
    a=int(input())
    if a == -1:
        break
    elif a==0:
        print(-pq.get())
    else:
        pq.put(-a)
