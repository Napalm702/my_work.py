def rus_apha(num):
    g = ''
    for i in range(len(ot_4)):
        g1 = 0
        for j in ot_4[i]:
            if j in rus_upper or j in rus_lower:
                for h in range(len(rus_upper)):
                    if j == rus_upper[h]:
                        g1 += h + ot_3
                        if g1 > len(rus_upper):
                            g1 = abs(len(rus_upper) - g1)
                            g += rus_upper[g1]
                            break
                        elif g1 == len(rus_upper):
                            g += rus_upper[g1 - 1]
                        else:
                            g += rus_upper[g1]
                            break

                    elif j == rus_lower[h]:
                        g1 += h + ot_3
                        if g1 > len(rus_lower):
                            g1 = abs(len(rus_lower) - g1)
                            g += rus_lower[g1]
                            break
                        elif g1 == len(rus_lower):
                            g += rus_lower[g1 - 1]
                        else:
                            g += rus_lower[g1]
                            break
            else:
                g += j
    return g
def eng_apha(num):
    g = ''
    for i in range(len(ot_4)):
        g1 = 0
        for j in ot_4[i]:
            if j in eng_lower or j in eng_upper:
                for h in range(len(eng_lower)):
                    if j == eng_lower[h]:
                        g1 += h + ot_3
                        if g1 > len(eng_lower):
                            g1 = abs(len(eng_lower) - g1)
                            g += eng_lower[g1]
                            break
                        elif g1 == len(eng_lower):
                            g += eng_lower[g1 - 1]
                        else:
                            g += eng_lower[g1]
                            break

                    elif j == eng_upper[h]:
                        g1 += h + ot_3
                        if g1 > len(eng_upper):
                            g1 = abs(len(eng_upper) - g1)
                            g += eng_upper[g1]
                            break
                        elif g1 == len(eng_upper):
                            g += eng_upper[g1 - 1]
                        else:
                            g += eng_upper[g1]
                            break
            else:
                g += j
    return g
def rus_apha_deshifr(num):
    g = ''
    for i in range(len(ot_4)):
        g1 = 0
        g2 = 0
        for j in ot_4[i]:
            if j in rus_upper or j in rus_lower:
                for h in range(len(rus_upper)):
                    if j == rus_upper[h]:
                        g1 += h - ot_3
                        if g1 > len(rus_upper):
                            g1 = abs(len(rus_upper) - g1)
                            g += rus_upper[g1]
                            break
                        elif g1 == len(rus_upper):
                            g += rus_upper[g1 - 1]
                        else:
                            g += rus_upper[g1]
                            break

                    elif j == rus_lower[h]:
                        g1 += h - ot_3
                        if g1 > len(rus_lower):
                            g1 = abs(len(rus_lower) - g1)
                            g += rus_lower[g1]
                            break
                        elif g1 == len(rus_lower):
                            g += rus_lower[g1 - 1]
                        else:
                            g += rus_lower[g1]
                            break
            else:
                g += j
    return g
def eng_apha_deshifr(num):
    g = ''
    for i in range(len(ot_4)):
        g1 = 0
        g2 = 0
        for j in ot_4[i]:
            if j in eng_lower or j in eng_upper:
                for h in range(len(eng_lower)):
                    if j == eng_lower[h]:
                        g1 += h - ot_3
                        if g1 > len(eng_lower):
                            g1 = abs(len(eng_lower) - g1)
                            g += eng_lower[g1]
                            break
                        elif g1 == len(eng_lower):
                            g += eng_lower[g1 - 1]
                        else:
                            g += eng_lower[g1]
                            break

                    elif j == eng_upper[h]:
                        g1 += h - ot_3
                        if g1 > len(eng_upper):
                            g1 = abs(len(eng_upper) - g1)
                            g += eng_upper[g1]
                            break
                        elif g1 == len(eng_upper):
                            g += eng_upper[g1 - 1]
                        else:
                            g += eng_upper[g1]
                            break
            else:
                g += j
    return g
def rus_alpha_spisok(num):  #осталось добавить пробелы после знаков препинания
    bryak = ''
    g1 = ot_4.split(' ')
    for i in range(1):
        for j in g1:
            bryak += ' '
            count = 0
            for h in j:
                if h.isalpha() == True:
                    if h in j:
                        count += 1
            for h in j:
                if h in rus_lower or h in rus_upper:
                    o = 0
                    for g in range(len(rus_lower)):
                        if h == rus_lower[g]:
                            o += g + count
                            if o > len(rus_lower):
                                o = abs(len(rus_lower) - o)
                                bryak += rus_lower[o]
                                break
                            elif o == len(rus_lower):
                                bryak += rus_lower[o - 1]
                            else:
                                bryak += rus_lower[o]
                                break

                        elif h == rus_upper[g]:
                            o += g + count
                            if o > len(rus_upper):
                                o = abs(len(rus_upper) - o)
                                bryak += rus_upper[o]
                                break
                            elif g1 == len(rus_upper):
                                bryak += rus_upper[o - 1]
                            else:
                                bryak += rus_upper[o]
                                break
                else:
                    bryak += h


    bryak = bryak.strip()
    return bryak
def eng_alpha_spisok(num):  #осталось добавить пробелы после знаков препинания
    bryak = ''
    g1 = ot_4.split(' ')
    for i in range(1):
        for j in g1:
            bryak += ' '
            count = 0
            for h in j:
                if h.isalpha() == True:
                    if h in j:
                        count += 1
            for h in j:
                if h in eng_lower or h in eng_upper:
                    o = 0
                    for g in range(len(eng_lower)):
                        if h == eng_lower[g]:
                            o += g + count
                            if o >= len(eng_lower):
                                o = abs(len(eng_lower) - o)
                                bryak += eng_lower[o]
                                break
                            elif o == len(eng_lower):
                                bryak += eng_lower[o - 1]
                            else:
                                bryak += eng_lower[o]
                                break

                        elif h == eng_upper[g]:
                            o += g + count
                            if o >= len(eng_upper):
                                o = abs(len(eng_upper) - o)
                                bryak += eng_upper[o]
                                break
                            elif g1 == len(eng_upper):
                                bryak += eng_upper[o - 1]
                            else:
                                bryak += eng_upper[o]
                                break
                else:
                    bryak += h


    bryak = bryak.strip()
    return bryak

print('шифрование - Y, дешифрование - N')
ot_1 = input()
print('Русский - R, английский - E')
ot_2 = input()
print('Шаг сдвига (вправо):')
ot_3 = int(input())
print('Введите текст:')
ot_4 = input()
g = ''
eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

if ot_1 == 'Y' or ot_1 == 'y':
    if ot_2 == 'R' or ot_2 == 'r':
        if ot_3 == 0:
            print(rus_alpha_spisok(ot_4))
        if ot_3 != 0:
            print(rus_apha(ot_4))
    elif ot_3 == 0:
        print(eng_alpha_spisok(ot_4))
    else:
        print(eng_apha(ot_4))

if ot_1 == 'N' or ot_1 == 'n':
    if ot_2 == 'R' or ot_2 == 'r':
        if ot_3 == 0:
            for k in range(1, 33):
                ot_3 = k
                print(rus_apha_deshifr(ot_4))
        print(rus_apha_deshifr(ot_4))
    else:
        if ot_3 == 0:
            for k in range(1, 26):
                ot_3 = k
                print(eng_apha_deshifr(ot_4))
        print(eng_apha_deshifr(ot_4))
