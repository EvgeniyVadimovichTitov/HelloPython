import random


def initoin_d(answers_user):
    if (
            answers_user == 'да' or answers_user == 'дА' or
            answers_user == 'Да' or answers_user == 'ДА' or
            answers_user == 'yes' or answers_user == 'Yes' or
            answers_user == 'YES' or answers_user == 'yES' or
            answers_user == 'yEs' or answers_user == 'yeS' or
            answers_user == 'da' or answers_user == 'Da' or
            answers_user == 'DA' or answers_user == 'dA'):
        k = input(
            'введите точность (в формате: 0.01/0,01 - два знака в десятичной части, \n' +
            'максимум 15 знаков):\n')
        if k[1] == ',':
            k = k.replace(',', '.')
    else:
        k = '0.'
        count = random.randint(1, 15)
        while count > 0:
            if count > 1:
                k += '0'
                count -= 1
            else:
                k += '1'
                count -= 1
        print(k)
    return k
