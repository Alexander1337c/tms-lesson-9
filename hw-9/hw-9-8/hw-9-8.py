import json
import csv


def get_data():
    with open('employees.json', 'r') as file:
        data = json.load(file)
        return data


def read_json():  # Чтение json и запись в csv
    data = get_data()
    save_csv(data)  # Вызов функции преобразования в csv


def save_csv(data_json):  # Непосредственно функция преобразования в csv
    with open('json_to_csv.csv', 'w') as file_csv:
        csv_file = csv.writer(file_csv)
        count = 0
        for data in data_json:
            if count == 0:
                header = data.keys()
                csv_file.writerow(header)
                count += 1
            csv_file.writerow(data.values())


def add_employee(name, birthday, height, weight, car, languages):  # Функция добавления сотрудника
    data = get_data()
    data.append({
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    })

    with open('employees.json', 'w') as json_file:
        json_file.write(json.dumps(data))
    save_csv(data)


def info_employees(name: str):  # Поиск информации о сотруднике по имени
    data = get_data()
    flag = True
    employees_arr = []
    for item in data:
        if name == item['name']:
            employees_arr.append(item)
            flag = False
    if flag:
        print(f"Сотрудника под именем {name} не существует")
    else:
        for i in employees_arr:
            print(i.values())


def filter_language(language: str):
    data = get_data()
    flag = True
    employees_arr = []
    for item in data:
        if language.strip() in item['languages'] or language.capitalize() in item['languages']:
            employees_arr.append(item)
            flag = False
    if flag:
        print(f"Сотрудников с ЯП {language} нет")
    else:
        for i in employees_arr:
            print(i.values())


def filter_age(year: str):
    data = get_data()
    flag = True
    avg_height = []
    for item in data:
        age_item = int(item['birthday'].split('.')[2])
        if int(year) > age_item:
            avg_height.append(item['height'])
            flag = False
    if flag:
        print(f"Сотрудников старше {year} года нет")
    else:
        print(f'Средний рост сотрудников старше {year} года - {sum(avg_height) / len(avg_height)}')


while True:
    dict_of_actions = {
        '1': '1. Добавить информацию о новом сотруднике',
        '2': '2. Получить информацию о сотруднике',
        '3': '3. Получить информацию о сотрудниках определенного ЯП',
        '4': '4. Узнать средний рост сотрудников по году',
        '5': '5. Завершить программу'
    }

    for i in dict_of_actions.keys():
        print(dict_of_actions[i])
    input_user = input('Выберите один из вариантов')
    if input_user:
        if input_user and dict_of_actions[input_user].split('. ')[0] == '1':
            name = input('Введите имя и фамилию через пробел')
            birthday = input('Дату рождения "20.12.2020"')
            height = input('Введите рост сотрудника')
            weight = input('Введите вес сотрудника')
            car = input('Наличие машины "true-есть, false-нет"')
            languages = input('Введите ЯП на которых работает сотруддник через пробел').split(' ')
            if name and birthday and height and weight and car and languages:
                add_employee(name, birthday, height, weight, car, languages)
            else:
                print('Не корректные данные')

        if input_user and dict_of_actions[input_user].split('. ')[0] == '2':
            name = input('Введите имя сотрудника: ')
            if name:
                info_employees(name)
            else:
                print("Некоректный ввод")

        if input_user and dict_of_actions[input_user].split('. ')[0] == '3':
            language = input('Введите ЯП: ')
            if language:
                filter_language(language)
            else:
                print("Некоректный ввод")

        if input_user and dict_of_actions[input_user].split('. ')[0] == '4':
            age = input('Введите год: ')
            if age:
                filter_age(age)
            else:
                print("Некоректный ввод")

        if input_user and dict_of_actions[input_user].split('. ')[0] == '5':
            print('Конец работы')
            break
    else:
        print('Такого варианта нет. Выберите один из доступных вариантов')
