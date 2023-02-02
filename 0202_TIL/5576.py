#콘테스트

w_list = [int(input()) for _ in range(10)]
k_list = [int(input()) for _ in range(10)]

w_sum = 0
k_sum = 0

w_list = sorted(w_list,reverse=True)
k_list = sorted(k_list,reverse=True)
for i in range(3):
    w_sum += w_list[i]
    k_sum += k_list[i]

print(w_sum, k_sum)