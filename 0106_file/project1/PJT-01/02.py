fruit_count = 0
with open('data/fruits.txt','r',encoding='UTF8') as f:
    for i in f:
        fruit_count = fruit_count+1
with open('02.txt','w',encoding='UTF8') as answer:
    answer.write(f'{fruit_count}')
