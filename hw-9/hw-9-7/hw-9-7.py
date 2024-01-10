result_arr = []
with open('data.txt', 'r') as file:
    lines = file.readlines()
    len_lines = len(lines)
    for i in range(len_lines):
        print(lines[i].strip())
        inc = i + 1
        tmp_str = ''
        for j in lines[i]:
            if j.isalpha():
                tmp_str += chr(ord(j) + inc)
        result_arr.append(tmp_str)

for i in result_arr:
    print(i)
