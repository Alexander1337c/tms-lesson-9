import os

print(f'Операционная система - {os.name}')
print(f'Текущая директория - {os.getcwd()}')
current_direrctory = os.getcwd()


def make_and_replace(extn: str, name):
    if os.path.exists(f'./{extn}_files'):
        os.replace(name, f'{extn}_files/{name}')
    else:
        os.mkdir(f'{extn}_files')
        os.replace(name, f'{extn}_files/{name}')


for i in os.listdir():
    base_name, base_extension = os.path.splitext(i)
    extension = base_extension.replace('.', '')
    if extension == 'csv':
        make_and_replace(extension, i)
    if extension == 'txt':
        make_and_replace(extension, i)
    if extension == 'json':
        make_and_replace(extension, i)

for i in os.listdir():
    if os.path.isdir(i):
        count_files = len(os.listdir(i))
        size_file = os.stat(i).st_size
        ext, _ = i.split('_')
        print(f"В папку с {ext} файлами перемещено {count_files} {tuple(os.listdir(i))} файлов общим размером {size_file} байт")
        if count_files > 1:
            old_name = os.listdir(i)[0]
            cur_dir = os.path.realpath(i)
            os.rename(f'{cur_dir}/{old_name}', f'{cur_dir}/new.txt')
            print(f"Файл {old_name} был переименован в {os.listdir(i)[0]}")





