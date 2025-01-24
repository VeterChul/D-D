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

list_r = ["s", "b", "r"]

R = 1

list_cub = []

list_com_1 = ["h", "all_h", "cls",      #"r", "h", "all_h", "cls", "all_buf", "", "n_R"]
list_com_2 = ["conf_buf", "buf", "c_buf", "ch_m"]

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
