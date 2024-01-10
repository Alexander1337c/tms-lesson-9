
tmp_dict = {}
with open('test.txt', 'r') as file_txt:
    text_join = ' '.join(file_txt.readlines())
    words = text_join.split(' ')
    for word in words:
        if word in tmp_dict:
            tmp_dict[word] += 1
        else:
            tmp_dict[word] = 1

with open('counter.txt', 'w', encoding='utf-8') as count_txt:
    tmp_arr = ''
    for k, v in tmp_dict.items():
        if v > 1:
            count_txt.write(f'Слово {k} встречается {tmp_dict[k]} раз \n')