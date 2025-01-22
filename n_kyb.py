import random as r

def test_kyb(k,ch = 1):
    return ch <= 40 and k <= 150 and ch > 0 and k > 0

def kyb(k, ch = 1):
    if not(k in [4, 6, 8, 10, 12, 20, 100, 3, 5]):
        print("Вы ввели куб не состоящий в стандартном наборе D&D. Проверте правильность ввода.", end="\n")
    for i in range(ch):
            if k == 10:
                n = r.randint(0, 9)    
                print("Ваше число:", n) 
            else:
                n = r.randint(1, k)
                print("Ваше число:", n) 
    return 0

def vib_r__(ky = "e"):
    global R, error_mess, old_s
    
    
    if ky == "e":
        print(error_mess, "Код ошибки 3")
        return 0
    elif ky == (0, 0):
        print("Вы ещё не вводили кубов")
        return 0
    elif R == "s":
        print("Вы кидаете куб 1k20")
        old_s = (1,20)
        kyb(20)
    else:
        print(f"Вы повторно кидаете куб {ky[0]}k{ky[1]}")
        kyb(ky[1], ky[0])

def vib_r_R(ky = "e"):
    global R, error_mess
    
    if ky == "e":
        print(error_mess, "Код ошибки 3")
        return 0
    if ky == (0, 0):
        print("Вы ещё не вводили кубов")
        return 0

    print(f"Вы повторно кидаете куб {ky[0]}k{ky[1]}")
    kyb(ky[1], ky[0])


R = "s"

def l_1(old_s):
    global R
    R = "r"
    return 0
def l_2(old_s):
    global R
    R = "s"
    return 0

def new_buf(ky):
    global list_cub
    print(f"Вы создали куб номер {len(list_cub) + 1} {ky[0]}k{ky[0]}")
    list_cub.append([ky[0], ky[1]])
    return 0

def conf_buf(n, ky):
    global list_cub
    if n > len(list_cub):
        print("Нет такого куба")
        return 0
    print(f"Вы заменили куб номер {n} {list_cub[n-1][0]}k{list_cub[n-1][1]} на куб {ky[0]}k{ky[1]}")
    list_cub[n -1] = [ky[0], ky[1]]
    return 0

def buf(n):
    global list_cub
    if n > len(list_cub):
        print("Нет такого куба")
    else:
        print(f"Вы кидаете куб {list_cub[n-1][0]}k{list_cub[n-1][1]}")
        kyb(list_cub[n-1][1], list_cub[n-1][0])
    
    return 0

def pr_all_buf():
    global list_cub
    if list_cub == []:
        print("У вас нет сохраненых кубов")
        return 0
    print("Вы сохранили следующие кубы:")
    for i in range(len(list_cub)):
        print(f"  Куб номер {i + 1}: {list_cub[i][0]}k{list_cub[i][1]}")
    return 0


list_cub = []

list_com_1_1 = ["r", "S", "h", "all_h", "cls", "R", "all_buf", "", "n_R"]
list_com_2_1 = ["conf_buf", "buf", "c_buf"]

def open_ky(ky):
    m = ky.split("k")
    return [int(m[0]), int(m[1])]



list_split = {
    'buf' : (lambda mas : (mas[0], (50, 160))),
    'conf_buf' : (lambda mas : (mas[0], open_ky(mas[1]))),
    'c_buf' : (lambda mas : (0, open_ky(mas[0]))),
}

list_com_1 = {
    'R' : (lambda old_s : l_1(old_s)),
    'S' : (lambda old_s : l_2(old_s)),
    'h' : (lambda old_s : print(h)),
    'all_h' : (lambda old_s : print(h_a)),
    'cls' : (lambda old_s : print("\n"*50)),
    'r' : (lambda old_s : vib_r_R(old_s)),
    '' : (lambda old_s : vib_r__(old_s)),
    'n_R' : (lambda old_s : print(R)),
    'all_buf' : (lambda old_s : pr_all_buf()),
    'buf' : (lambda n, ky : buf(n)),
    'conf_buf' : (lambda n, ky : conf_buf(n, ky)),
    'c_buf' : (lambda n, ky : new_buf(ky)),
    }

start_mess = "Преветствуем путешествиники или мастера  в симуляторе кубов D&D.\nЧтобы прочесть инструкцию введите 'h'"
error_mess = "Произошла техническая ошибка.\nВведите куб повторно или 'h' для порлучения справки"

list_c =     "    h - подсказака\
            \n    all_h - большая подсказка\
            \n    cls - очистка терминала\
            \n    r - вывести последний куб\
            \n    n_R - вывест режим в котором вы находитесь сейчас"

list_c_b =   "    all_buf - вывести заполненые сохраненые кубы\
            \n    buf n - кинуть n-ный сохранённый куб\
            \n    c_buf mki- создать новый куб, где m - это число кубов, а i это номенал куба\
            \n    conf_buf n mki- обновить значение n-ного сохраненого куба на куб где m - это число кубов, а i это номенал куба"

list_ptin =  "    all_buf\
            \n    buf 1\
            \n    c_buf 3k4\
            \n    conf_buf 1 2k4"

s_r = "S - режим, когда при нажатии Enter выводится куб 1k20"
r_r = "R - режим, когда при нажатии Enter выводится последний введеный куб"

h_a = f"Введите два числа. Первое - количество кубов, второе - значение. Первое вводить необязательно.\
            \nНапример:\n    Запрос 2k6: 2 6\n    Запрос: 1k4: 4\n\
            \nОграничения:\n    Максимальный номинал куба 150\n    Максимальное количество кубов 40\n\
            \nДля выхода введите 'q'\
            \n\nРежимы:\
            \n    {s_r}\
            \n    {r_r}\
            \nДля выбора режима введите его название\
            \n\nСписок команд:\
            \n{list_c}\
            \n\nСохраненные кубы(пока не дописано):\
            \nВы можете сохранить до 15 кубов, которые можно кинуть одной командой.\
            \nКоманды для работы с сохранёнными кубами\
            \n{list_c_b}\
            \n Примеры использования команд:\
            \n{list_ptin}"

h = f"Введите два числа. Первое - количество кубов, второе - значение. Первое вводить необязательно.\
            \nНапример:\n    Запрос 2k6: 2 6\n    Запрос: 1k4: 4\n\
            \nОграничения:\n    Максимальный номинал куба 150\n    Максимальное количество кубов 40\n\
            \nДля выхода введите 'q'\
            \n\nРежимы:\
            \n    S - Выйти в стандартный режим\
            \n    R - Режим повтора последнего введеного куба\
            \nДля выбора режима введите его название\
            \n\nСписок команд:\
            \n{list_c}\
            \n{list_c_b}"

print(start_mess)

s = input()
old_s = (0, 0)

while s != 'q':
	try:
		chit = s[0] == " "
		s = s.split()
		if s[0] in list_com_1_1:
			print(1)
		elif s[0] in list_com_2_1:
			print(2)
		else:
			print(3)
	
	except:
		print(error_mess,"Ошибка не известна, код 1")
	finally:
		s = input()

print("Спасибо, что воспользовались программой. Желаем ещё собраться за столом")
