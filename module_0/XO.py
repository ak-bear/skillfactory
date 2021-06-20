field = ([' ', '1', '2', '3'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-'],
         ['3', '-', '-', '-']
        )
def out(f): 
    """вывод поля"""
    for i in range(4):
        print(" ".join(f[i]))
    return

def check( cor, f ):   
    """проверка хода"""
    if cor.isdigit() and len(cor)==2:
        h = int(cor)//10
        v = int(cor)%10
        return h in range(1,4) and v in range(1,4) and f[h][v]=='-' 
    else:
        return False
            
def marc(n): 
    """маркер текущего хода"""
    if n%2 == 0:
        stn = 'нолики'
    else: stn = 'крестики'
    return stn

def step( n, hv , f ): 
    """ход"""
    h = int(hv)//10
    v = int(hv)%10
    if n%2 == 0:
        f[h][v] = '0'
    else: f[h][v] = 'X'
    n=n+1
    return n,f

def win (f): 
    """проверка победы - три элемента в ряд"""
    w = False
    for i in range(1,4):
        if f[i].count('0')==3 or f[i].count('Х')==3: #не понял причины, но исправление этой конструкции на ваш вариант нарушает работу всей функции
            w = True  
        a = (f[1][i],f[2][i],f[3][i]).count('0')         
        b = (f[1][i],f[2][i],f[3][i]).count('X')
        if a == 3 or b == 3:
            w = True
    c = (f[1][1],f[2][2],f[3][3]).count('0')          
    d = (f[1][1],f[2][2],f[3][3]).count('X')
    e = (f[3][1],f[2][2],f[1][3]).count('0')
    g = (f[3][1],f[2][2],f[1][3]).count('X')
    if any([c == 3, d == 3, e == 3, g == 3]):
        w = True
    return w

def game (var):
    """собственно игра"""
    if var == 'y':
        print('Отлично! Координаты хода вводятся без пробела в порядке строка-столбец')
        print()
        for n in range(1,10):
            out(field)
            print()
            print ('ход №', n, ' (',marc(n),')')
            hv = input()
            while check(hv, field) == False:
                print('Невозможный ход/неверный ввод')
                hv = input()
            step(n, hv, field)
            if n > 4 and win(field):
                out(field)
                print('Победа! (',marc(n),')')
                break
        if n == 9 and win(field) == False: print('Ничья')
    else:
        print ('Жаль. До свидания!')
    
yes = str(input('Сыграем в крестики-нолики? (y) ',))
game(yes)