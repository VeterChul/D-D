import random as r
from inscriptions import start_mess, error_mess, list_c, list_c_b, list_ptin , h_a, h

def test_kyb(k,ch = 1):
    return ch <= 40 and k <= 150 and ch > 0 and k > 0

def mass(n):
    m = []
    for i in range(n):
        for j in range(i):
            m.append(i+1)
    return r.choice(m)


def kyb(k, ch = 1, chit = False):
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
    return 0

def throw_again():#перекинуть последний куб
    pass

def svipe_mode(n_mode):#сменить мод
    global list_mode, mode
    mode = list_mode.index(n_mode)
    return 0

def print_saved(mas):
    global list_cub
    if mas == []:
        mas = [0, len(list_cub) - 1]
    print("У вас есть сохранёные кубы:")
    for i in range(mas[0]-1, mas[1]):
        print(f"    {i}:{list_cub[i][0]}k{list_cub[i][1]}")

def new_cub(mas):
    pass

def __again():
    pass

def throw(mas):
    pass

list_mode = ["s", "b", "r"]

mode = 1

list_cub = []

list_com = ["ch_m", "cls", "help", "mode", "again",  "saved", "save", "", "throw"]
list_def = {
    'ch_m' : (lambda mas : print(list_mode[mode])),
    'cls' :  (lambda mas : print("\n"*50)), 
    'help' : (lambda mas : print(h)),
    'mode' : (lambda mas : svipe_mode(mas[0])),
    'again'  : (lambda mas : throw_again()),
    'saved' : (lambda mas : print_saved(mas)),
    'save' : (lambda mas : new_cub(mas)),
    '' : (lambda mas : __again()),
    'throw' : (lambda mas : throw(mas)),
    }

def open_ky(ky):
    m = ky.split("k")
    return [int(m[0]), int(m[1])]



list_split = {
    'buf' : (lambda mas : (mas[0], (50, 160))),
    'conf_buf' : (lambda mas : (mas[0], open_ky(mas[1]))),
    'c_buf' : (lambda mas : (0, open_ky(mas[0]))),
}

print(start_mess)

s = input()
old_s = (0, 0)

while s != 'q':
	try:
		chit = s[0] == " "
		s = s.split()
		if s[0] in list_com:
			pass
		else:
			print(3)
	
	except:
		print(error_mess,"Ошибка не известна, код 1")
	finally:
		s = input()

print("Спасибо, что воспользовались программой. Желаем ещё собраться за столом")
