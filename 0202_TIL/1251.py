# 단어 나누기

word = input()
answer = []
for i in range(len(word)-2):
    for j in range(i+1,len(word)-1):
        for k in range(j+1,len(word)):
            #[맨앞 / 중간 / 맨뒤] [뒤에서부터 출력]
            ans = word[0:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            if ans not in answer:
                answer.append(ans)
print(sorted(answer)[0])