with open('data/fruits.txt','r',encoding='UTF8') as f:
    fruit_count = 0
    berry = {}
    for berry_i in f:
        if berry_i in berry.keys():
            berry[berry_i]+=1
        elif berry_i not in berry.keys():
            berry[berry_i] = 1
    with open('04.txt','w',encoding='UTF8') as answer:
        for key, value in berry.items():
            key = key.replace('\n','')
            answer.write(f'{key} {value}\n')