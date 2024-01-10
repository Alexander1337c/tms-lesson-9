start_str = '123 ааа456 1x2y3z 4 5 6'
integer = []
i = 0

while i < len(start_str):
    tmp_str = ''
    while i < len(start_str) and '0' < start_str[i] < '9':
        tmp_str += start_str[i]
        i += 1
    i += 1
    if tmp_str:
        integer.append(int(tmp_str))

print(sum(integer))
