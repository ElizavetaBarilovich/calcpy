# скобка открывается пять плюс шесть умножить на семь
def calc(text):
    """ Функиця принимает текстовое математическое выражение. Возвращает результат оперции в словестном виде.
        Можно использовать скобки, математические опрации: плюс, минус, умножить"""
    text = text.strip()
    textn = text
    wordDict = {'скобка': '', 'открывается': '(', 'закрывается': ')', 'умножить': '*', 'на': '', 'плюс': '+',
                'минус': '-',
                'ноль': '0', 'один': '1', 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5', 'шесть': '6', 'семь': '7',
                'восемь': '8', 'девять': '9', 'десять': '10', 'одиннадцать': '11',
                'двенадцать': '12', 'тринадцать': '13', 'четырнадцать': '14', 'пятнадцать': '15',
                'шестнадцать': '16', 'семнадцать': '17', 'восемнадцать': '18', 'девятнадцать': '19',
                'двадцать': '20', 'тридцать': '30', 'сорок': '40', 'пятьдесят': '50', 'шестьдесят': '60',
                'семьдесят': '70',
                'восемьдесят': '80', 'девяносто': '90', 'сто': '100', 'двести': '200', 'триста': '300',
                'четыреста': '400', 'пятьсот': '500', 'шестьсот': '600', 'семьсот': '700', 'восемьсот': '800',
                'девятьсот': '900', 'одна тысяча': '1000', 'две тысячи': '2000', 'три тысячи': '3000',
                'четыре тысячи': '4000', 'пять тысяч': '5000', 'шесть тысяч': '6000', 'семь тысяч': '7000',
                'восемь тысяч': '8000', 'девять тысяч': '9000'}
    revwordDict = {v: k for k, v in wordDict.items()}
    revwordDictkeys = list(revwordDict)
    wordDictkeys = list(wordDict)[::-1]
    textsp = text.split(' ')
    flag = False
    for word in range(len(textsp)):
        if textsp[word] in wordDictkeys:
            if wordDict[textsp[word]].isnumeric():
                if flag == True:
                    flag = False
                elif int(wordDict[textsp[word]]) < 20 or word == len(textsp):
                    textn = textn.replace(textsp[word], wordDict[textsp[word]], 1)
                elif int(wordDict[textsp[word]]) >= 20:
                    if textsp[word + 1] not in revwordDictkeys:
                        return 'Введеное значение содержит лишние символы'
                    elif wordDict[textsp[word + 1]].isnumeric():
                        textn = textn.replace(textsp[word] + ' ' + textsp[word + 1],
                                              str(int(wordDict[textsp[word]]) + int(wordDict[textsp[word + 1]])), 1)
                        flag = True
            else:
                textn = textn.replace(textsp[word], wordDict[textsp[word]], 1)
    for el in textn.split():
        if el not in revwordDictkeys:
            return 'Введеное значение содержит лишние символы'
    if textn.count('(') != textn.count(')'):
        return 'Введеное значение содержит незакрывающиеся скобки'
    resint = eval(textn)
    result = ''
    if resint < 0:
        result += 'минус '
        resint = abs(resint)
    if resint >= 0 and resint <= 20:
        print(revwordDict[str(resint)])
    else:
        for num in range(len(str(resint))):
            mult = int(str(resint)[num]) * int('1' + '0' * (len(str(resint)) - num - 1))
            if mult == 0:
                pass
            else:
                result += revwordDict[str(mult)] + ' '
    return (result)


text = input('Пожалуйста, введите строковое выражение для калькулятора: ')
print(calc(text))
