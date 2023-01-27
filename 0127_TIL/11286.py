#절댓값 힙
import heapq
import sys

N = int(sys.stdin.readline())


x_list=[]
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(x_list,(abs(x),x))        
    else:
        if x_list == []:
            print(0)
        else:
            print(heapq.heappop(x_list)[1])