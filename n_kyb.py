import random as r
#from inscriptions import start_mess, error_mess, h_a, h

start_mess = "Преветствуем путешествиники или мастера  в симуляторе кубов D&D.\nЧтобы прочесть инструкцию введите 'h'"
error_mess = "Произошла техническая ошибка.\nВведите куб повторно или 'h' для порлучения справки"

list_mode = ["s", "b", "r"]

mode = 0

list_cub = []

list_com = ["ref", "ch_m", "cls", "help", "mode", "again",  "saved", "save", "", "throw"]
list_def = {
    'ch_m' : (lambda mas : print(list_mode[mode])),
    'cls' :  (lambda mas : print("\n"*50)), 
    'help' : (lambda mas : print_help()),
    'ref' :  (lambda mas : print_ref()),
    'mode' : (lambda mas : svipe_mode(mas[0])),
    'again' : (lambda mas : throw_again()),
    'saved' : (lambda mas : print_saved(mas)),
    'save' : (lambda mas : new_cub(mas)),
    '' : (lambda mas : __again(mas)),
    'throw' : (lambda mas : throw(mas)),
    }

s = input()
old_s = (0, 0)


def test_kyb(k,ch = 1):
    return ch <= 40 and k <= 150 and ch > 0 and k > 0

def mass(n):
    m = []
    for i in range(n):
        for j in range(i*i):
            m.append(i+1)
    return r.choice(m)


def kyb(k, ch = 1, chit = False):
    global old_s
    if not(k in [4, 6, 8, 10, 12, 20, 100, 3, 5]):
        print("Вы ввели куб не состоящий в стандартном наборе D&D. Проверте правильность ввода.", end="\n")
    for i in range(ch):
            if chit:
                n = mass(k)
            else:
                n = r.randint(1, k)
            if k == 100:
                    n -= 1        
            print("Ваше число:", n) 
            old_s = (ch, k)
    return 0

def svipe_mode(mas):#сменить мод
    global mode, list_mode, error_mess
    try:
        mode = list_mode.index(mas[0])
    except:
        print(error_mess, "Ошибка изменения мода. Проверьте првильность ввода.\nНапишите ref для получения справки.")

def print_saved(mas):
    global list_cub
    if len(mas) == 1:
        mas = [0, len(list_cub) - 1]
    print("У вас есть сохранёные кубы:")
    for i in range(mas[0]-1, mas[1]):
        print(f"    {i}:{list_cub[i][0]}k{list_cub[i][1]}")

def new_cub(mas):#создать новый куб
    pass

def __again(mas):#ентер
    global mode, old_s
    if mode == 0:
        kyb(20, 1, mas[-1])
    else:
        kyb(old_s[1], old_s[0], mas[-1])

def throw(mas):#кинуть сохраненый куб
    global mode, list_cub
    kybb = list_cub[mas[0]]
    kyb(kybb[1], kybb[0], mass[-1])

def throw_again(mas):#перекинуть последний куб
    global old_s
    kyb(old_s[1], old_s[0], mas[-1])

def print_help():
    global list_mode, mode
    h = f"Вы находитесь в режиме {list_mode[mode]}.\nДля получения справки пропишите 'ref'"
    print(h)
    return 0

def print_ref():
    global list_mode, mode
    h = "Заглушка"
    print(h)
    return 0

def open_ky(ky):
    m = ky.split("k")
    return [int(m[0]), int(m[1])]

print(start_mess)

while s != 'q':
    try:
        chit = s[0] == " "
        s = s.split()
        if mode in (0, 2):
            if s[0] in list_com:
                list_def[s[0]](s[1:].append(chit))
            else:
                if len(s) == 1:
                    kyb(int(s[0]), chit = chit)
                else:
                    kyb(int(s[1]), int(s[0]), chit = chit)
        elif mode in (1, ):
            throw([s[0], chit])
    except:
        print(error_mess,"Ошибка не известна, код 1") 
    finally:
        s = input()

print("Спасибо, что воспользовались программой. Желаем ещё собраться за столом")
