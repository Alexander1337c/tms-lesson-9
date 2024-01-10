import random

first_name = ['Maxim', 'Alexander', 'Nikita', 'Pavel']
last_name = ['Sidorov', 'Smirnov', 'Kucher', 'Babich']

student = [{
    'first_name': random.choice(first_name),
    'last_name': random.choice(last_name),
    'point': random.randint(1, 6),
} for i in range(5)]

with open('student_info.txt', 'w') as file:
    for i in student:
        file.writelines(f"{i['first_name']} {i['last_name']} {i['point']}\n")

with open('student_info.txt', 'r') as file:
    info = file.readlines()
    student_board = []
    for i in info:
        res = i.split(' ')
        student_board.append({'first_name': res[0], 'last_name': res[1], 'point': res[2]})
    result = list(filter(lambda item: int(item['point']) > 3, student_board))


print('Список студентов')
[print(f'{i["first_name"]} {i["last_name"]} {i["point"].strip()}') for i in student_board]
print('Список студентов с оценкой выше 3')
[print(f'{i["first_name"]} {i["last_name"]} {i["point"].strip()}') for i in result]
