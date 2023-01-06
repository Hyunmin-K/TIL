with open('data/fruits.txt','r',encoding='UTF8') as f:
    fruit_count = 0
    berry = []
    for i in f:
        if i[-6:-1] == 'berry' and i not in berry:
            berry.append(i)
            fruit_count +=1
    with open('03.txt','w',encoding='UTF8') as w:
        w.write(f'{fruit_count}\n')
        for answer in berry:
            w.write(answer)
with open('03.txt','w',encoding='UTF8') as answer:
    answer.write(f'{fruit_count}')
    for i in berry:
        answer.write(i)