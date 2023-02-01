# 점수 집계

T = int(input())
for i in range(T):
    n = list(map(int,input().split()))
    n.remove(max(n))
    n.remove(min(n))
    if max(n) - min(n) >=4:
        print('KIN')
    else:
        print(sum(n))
    
# T = int(input())
# for i in range(T):
#     n = list(map(int,input().split()))
#     sort_n = sorted(n)
#     if sort_n[len(n)-2] - sort_n[1] >=4:
#         print('KIN')
#     else:
#         print(sum(sort_n)-sort_n[0]-sort_n[len(n)-1])

#오른쪽, 왼쪽 pop
# T = int(input())

# for _ in range(T):
#     scores = list(map(int, input().split()))
#     # 0. 기존처럼 최고점, 최저점을 리스트에서 제외하라.

#     scores.sort() # 최고점이 오른쪽
#     scores.pop() # 최고점 제거
#     scores.pop(0) # 최저점 제거
#     # print(scores)

#     # 1. 점수를 조정할 필요가 없으면(즉, 나머지 3명의 최고점 최저점 차가 4점 미만이면) -> 이전 방식으로 출력
    
#     if scores[2] - scores[0] < 4:
#         print(sum(scores))

#     # 2. 점수를 조정해야 한다면(즉, 나머지 3명의 최고점 최저점 차가 4점 이상이면) -> KIN 출력
#     else:
#         print('KIN')