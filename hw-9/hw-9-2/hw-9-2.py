
input_text = '''Подсудимая Эверт-Колокольцева Елизавета Александровна
 в судебном заседании вину инкриминируемого
 правонарушения признала в полном объёме и суду показала,
 что 14 сентября 1876 года, будучи в состоянии алкогольного
 опьянения от безысходности, в связи с состоянием здоровья
 позвонила со своего стационарного телефона в полицию,
 сообщив о том, что у неё в квартире якобы заложена бомба.
 После чего приехали сотрудники полиции, скорая
 и пожарные, которым она сообщила, что бомба — это она.'''


def change_name(text: str, new_name: str):
    if new_name.istitle():
        N = new_name.split(' ')
        split_text = text.split(' ')
        for i in range(3):
            split_text[i + 1] = N[i]
        res = ' '.join(split_text)
        print(res)
    else:
        print('ФИО может начинаться только с заглавных букв')


change_name(input_text, 'Nikola Guns-Mashine Albert')