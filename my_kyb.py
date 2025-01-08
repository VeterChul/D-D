import random as r

def kyb(k, ch = 1, P = False):

    if ch <= 40 and k <= 150 and ch > 0 and k > 0:
        if not(k in [4, 6, 8, 10, 12, 20, 100, 3, 5]):
            print("Вы ввели куб не состоящий в стандартном наборе D&D. Проверте правильность ввода.", end="\n")
        for i in range(ch):
                if k == 10:
                    m = [i+1 for i in range(k)]
                    if P:
                        for i in range((3*k)/(k+1)):
                            m.append(k-1)
                    n = m[r.randint(1, len(m))]
                    
                    n = r.randint(0, 9)    
                    print("Ваше число:", n) 
                else:
                    m = [i+1 for i in range(k)]
                    if P:
                        for i in range((3*k)/(k+1)):
                            m.append(k)
                    n = m[r.randint(1, len(m))]
                    print("Ваше число:", n) 

    else:
        print("Произошла техническая ошибка.\n    Значения не попадают в допустимые значения.\nВведите куб повторно или 'help' для порлучения справки.")
    
    return 0

print("Преветствуем путешествиники или мастера  в симуляторе кубов D&D.\nЧтобы прочесть инструкцию введите 'help'")

P = False
s1 = input()
if s1[0] == ' ':
    P = True
s = s1.split()

while s != ['e']:
    try:
        if s == ["help"]:
            print("Введите два числа. Первое это количество кубов, второе это значение. Первое вводить необязательно.\
                        \nНапример:\n    Запрос 2k6: 2 6\n    Запрос: 1k4: 4\n\
                        \nОграничения:\n    Максимальный номинал куба 150\n    Максимальное количество кубов 40\n\
                        \nДля выхода введите 'e'")
        elif len(s) == 2:
            kyb(int(s[1]), int(s[0]), P)
        else:
            kyb(int(s[0]), P)
    except:
        print("Произошла техническая ошибка. Введите куб повторно или 'help' для порлучения справки.")
    finally:
        s = input().split()
        P = False
        s1 = input()
        if s1[0] == ' ':
            P = True
        s = s1.split()

print("Поблагодарите друг друга за игру")
