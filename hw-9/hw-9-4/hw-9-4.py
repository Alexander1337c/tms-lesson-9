
def replace_dirty_words(name_files: str):
    with open('stop_words.txt', 'r') as stop:
        line = stop.readline()
        words = line.split(' ')

    with open(name_files, 'r') as check:
        lines = ' '.join(check.readlines()).split(' ')
        len_arr = len(lines)
        for i in range(len_arr):
            for word in words:
                if word in lines[i].lower():
                    lines[i] = lines[i].lower().replace(word, '*' * len(word))
        result = ' '.join(lines)
        print(result)


replace_dirty_words('text_for_check.txt')
