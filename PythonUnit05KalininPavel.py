# Калинин Павел 15.01.2023 
# Знакомство с языком Python (семинары) 
# Урок 5. 
# Домашняя работа

from random import randint
from time import sleep

taskName = '''Задание  №1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
           '''
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    substr = 'абв'
    print("Текст из файла file3.txt")
    text1: str 
    with open('file3.txt', 'r', encoding='utf-8') as f:
        text1 = f.read()
    print("-"*20)
    print(text1)
    print("-"*20)
    list1 = text1.split()
    list_items = []
    for i, item in enumerate(list1):
        if substr in item: list_items.append(i)
    for i in list_items[::-1]:
        del list1[i]
    #--------------
    print('Ответ:')
    print(' '.join(list1))
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s and s != '0'
#------


# неумелая попытка сделать русские окончания у конфет
def candy_by_rus(qty, a=0): # а=0 '..а' а=1 '..у' для хх1 
    candy = 'конфет'
    if str(qty)[-1] == '1':
        if a == 1:
            candy = 'конфету'
        else:    
            candy = 'конфета'
    elif str(qty)[-1] in ['2','3','4']:
        candy = 'конфеты'
    return candy  


taskName = '''Задание  №2. 
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
  чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'
           '''
isRepeat = True
while(isRepeat): 
    print("")
    print("")
    print("")
    print("-----------------------------------\n\r"+taskName)
    PEOPLE_PEOPLE = ('Человек с человеком',)
    PEOPLE_BOT    = ('Человек с ботом',)
    BOT_BOT       = ('бот с ботом',)
    TYPE_GAME = (PEOPLE_PEOPLE,PEOPLE_BOT,BOT_BOT)

    text = ['Выберите режим игры:\n']
    for i, el in enumerate(TYPE_GAME):
        text.append(f'{i+1} - {TYPE_GAME[i][0]}\n') 
    text.append(':')
    type_int = int(input(''.join(text))) # спросить у пользователя кто играет
    type_of_game = TYPE_GAME[type_int-1]

    # Имена игроков спрашивать не буду. Оставлю по умолчанию. 
    #    Не актуально. Сэкономлю время.
    PLAYER_1 = ('Игрок №1',)
    PLAYER_2 = ('Игрок №2',)
    PLAYERS = (PLAYER_1,PLAYER_2)
    # связка игроков и их типов (человек или бот)
    LINK_PLAYER_AND_TYPE_PLAYER = {PLAYER_1:None, PLAYER_2:None}

    PLAYER_PEOPLE = ('Человек',)
    PLAYER_BOT    = ('Бот',)

    if   type_of_game == PEOPLE_PEOPLE:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_1] = PLAYER_PEOPLE
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_2] = PLAYER_PEOPLE
    elif type_of_game == PEOPLE_BOT:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_1] = PLAYER_PEOPLE
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_2] = PLAYER_BOT
    elif type_of_game == BOT_BOT:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_1] = PLAYER_BOT
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_2] = PLAYER_BOT
    #-----------------------------------------

    r = randint(0,len(PLAYERS)-1) # жеребьёвка между всеми игроками
    curr_player = PLAYERS[r] # игрок начинающий игру
    name = f'{curr_player[0]} ({LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]})'
    print(f'После жеребьёвки первым делает ход {name}')

    number_move = 1 # номер хода

    qty_all = int(input('Введите кол-во конфет - натуральное число: '))
    step = int(input('Введите кол-во конфет,'
          +' которое можно забрать за один ход - натуральное число: '))
    rest = qty_all # столько конфет лежит на столе.
    win_qty = rest - (step+1) * ( rest//(step+1) ) # кол-во конфет должен взять игрок

    if win_qty > 0: 
        print('Сколько конфет нужно взять первому игроку,'
              +' чтобы забрать все конфеты у своего конкурента? - '+str(win_qty)
              +' '+ candy_by_rus(win_qty, 1) + '.')
    else: # нет решения, проигрыное начало
        print('Сколько конфет нужно взять первому игроку,'  
              + ' чтобы забрать все конфеты у своего конкурента? - Нет такого возможности.')
        win_qty = step # чтобы не тянуть резину

    check = 0 # самоконтроль
    print(f'Начало игры. На столе лежит {rest} конфет.')

    people_moves = [] # запомнить как ходит человек; для проверки на однотипные ходы
    button_stuck = False # однотипные ходы человека - клавиатура залипла или мозги
    qty = 0  # кол-во конфет, которые будут взяты со стола игроком на текущем ходу

    # главный цикл, пока конфеты есть на столе
    while(rest > 0):
        # расчет выгрышного хода; если человек раз ошибется, то ...
        win_qty = rest - (step+1) * ( rest//(step+1) ) 
        # заполнение флага однотипных ходов
        if len(people_moves)>1 and people_moves[-1] == people_moves[-2]:  
            button_stuck = True
        else: button_stuck = False
        #print('win=',qty, 'people_moves=',people_moves,'button_stuck=',button_stuck)
        # если проигрышное начало и человек ходит однотипно - 
        #   не залипать самому на максимальном значении
        if button_stuck and step > 1: 
            qty   = win_qty if win_qty > 0 else step-1 # взять меньше макс., если человек залип
        else: qty = win_qty if win_qty > 0 else step   # взять максимум конфет, чтобы не тянуть
        max_candy_for_take = step if rest >= step else rest

        name = f'{curr_player[0]} ({LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]})'
        text_bot    = f'Ход {number_move}. {name} забирает {qty} {candy_by_rus(qty,1)}.'
        text_people = f'Ход {number_move}. {name} сколько конфет вы хотите забрать? :'

        # ввод данных
        if LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_PEOPLE:
            while(True): # ожидание правильных данных от человека
                qty = int(input(text_people))
                if 1 <= qty <= max_candy_for_take: break
            people_moves.append(qty) # ..., но будет использоваться только если один бот
        elif LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_BOT:
            sleep(1)
            print(text_bot)

        rest -= qty # оставшихся конфет на столе стало меньше
        print(f'На столе осталось {rest} {candy_by_rus(rest)}.')
        curr_player = PLAYER_1 if curr_player == PLAYER_2 else PLAYER_2  # смена игрока
        number_move += 1  # номер хода увеличить
        check += qty
    #------------------------------------------------------------    
    # для определения игрока, который ходил последним
    curr_player = PLAYER_1 if curr_player == PLAYER_2 else PLAYER_2 
    name = f'{curr_player[0]} ({LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]})'
    print('-'*20)
    print(f'{name} выиграл и забирает все конфеты!')
    print('-'*20)
    if check != qty_all: print(f'Ошибка. Игроки взяли со стола {check} конфет.') 
    #--------------
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s and s != '0'
#------











def print_playing_field(playing_field):
    a = playing_field
    print('')
    print(f'_0|1|2_   ||   _{a[0]}|{a[1]}|{a[2]}_')
    print(f'_3|4|5_   ||   _{a[3]}|{a[4]}|{a[5]}_')
    print(f' 6|7|8    ||    {a[6]}|{a[7]}|{a[8]}')
    print('')

def check_win_combo(playing_field, WIN_COMBOS, X,O):
    # набор ячеек с Х
    setX = {i for i, el in enumerate(playing_field) if el == X}
    for line in WIN_COMBOS: 
        if len(line & setX) == 3: return X
    # набор ячеек с O
    setO = {i for i, el in enumerate(playing_field) if el == O}
    for line in WIN_COMBOS: 
        if len(line & setO) == 3: return O
    return None

# наити наилучший ход для бота
# 1 - найти выигрышную линию с двумя заполненными ячейками и одной пустой
# 2 - иначе, найти такую же у противника и заблокировать ее 
# 3 - иначе, найти линии с одной заполненной ячейкой и двумя пустыми
#     и пересечь ее с априоным рейтингом ячеек и выбрать максимум из остатка
# все это с учетом того, что непреемлемые варианты сразу удаляются в списках:
#     win_combos_X, win_combos_O, rating_cell   
def find_better_move(playing_field, curr_player, PLAYER_X, PLAYER_O 
                     , win_combos_X, win_combos_O, rating_cell, X, O):

    setX = {i for i, el in enumerate(playing_field) if el == X} # набор ячеек с Х
    setO = {i for i, el in enumerate(playing_field) if el == O} # набор ячеек с O

    list_2P = set() # список ячеек в линиях где заполнена 1 ячейка для текущего игрока

    if curr_player == PLAYER_X:
        # найти свою выигрыную линию (2 заполнены)
        for line in win_combos_X: 
            if len(line & setX) == 2: # линия с двумя Х и одной пустой
                l = line - setX
                return l.pop() # выигрышный 3-ий номер в линии для Х
        # если нет своей выигрышной линии, найти и заблокировать у О        
        for line in win_combos_O: 
            if len(line & setO) == 2: # линия с двумя O и одной пустой
                l = line - setO
                return l.pop() # выигрышный 3-ий номер в линии для O
        # найти предзаполненную линию (1 заполнена)
        for line in win_combos_X: 
            if len(line & setX) == 1: # линия с одним Х и двумя пустыми
                list_2P |= (line - setX) # пустой 2-ий и 3-ий номера в линии для Х

    elif curr_player == PLAYER_O: # все тоже самое но для O

        # найти свою выигрыную линию (2 заполнены)
        for line in win_combos_O: 
            if len(line & setO) == 2: # линия с двумя O и одной пустой
                l = line - setO
                return l.pop() # выигрышный 3-ий номер в линии для O
        # если нет своей выигрышной линии, найти и заблокировать у X        
        for line in win_combos_X: 
            if len(line & setX) == 2: # линия с двумя X и одной пустой
                l = line - setX
                return l.pop() # выигрышный 3-ий номер в линии для X
        # найти предзаполненную линию (1 заполнена)
        for line in win_combos_O: 
            if len(line & setO) == 1: # линия с одним O и двумя пустыми
                list_2P |= (line - setO) # пустой 2-ий и 3-ий номера в линии для O

    if list_2P:
        cell_with_max_rating = -1
        for n in list_2P:
            if rating_cell[n] > cell_with_max_rating:
                cell_with_max_rating = n
        return cell_with_max_rating if cell_with_max_rating >= 0 else None
    else: 
        cell_with_max_rating = -1
        max_rating_cell = max(rating_cell)
        for n in rating_cell:
            if rating_cell[n] == max_rating_cell:
                cell_with_max_rating = n
        return cell_with_max_rating if cell_with_max_rating >= 0 else None


taskName = '''Задание  №3. Создайте программу для игры в ""Крестики-нолики"".
           '''
isRepeat = True
while(isRepeat): 
    print("")
    print("")
    print("")
    print("-----------------------------------\n\r"+taskName)
    PEOPLE_PEOPLE = ('Человек с человеком',)
    PEOPLE_BOT    = ('Человек с ботом',)
    BOT_BOT       = ('бот с ботом',)
    TYPE_GAME = (PEOPLE_PEOPLE,PEOPLE_BOT,BOT_BOT)

    text = ['Выберите режим игры:\n']
    for i, el in enumerate(TYPE_GAME):
        text.append(f'{i+1} - {TYPE_GAME[i][0]}\n') 
    text.append(':')
    type_int = int(input(''.join(text))) # спросить у пользователя кто играет
    type_of_game = TYPE_GAME[type_int-1]

    # Имена игроков спрашивать не буду. Оставлю по умолчанию. 
    #    Не актуально. Сэкономлю время.
    PLAYER_X = ('Игрок КРЕСТИК',)
    PLAYER_O  = ('Игрок НОЛИК',)
    PLAYERS = (PLAYER_X,PLAYER_O)
    # связка игроков и их типов (человек или бот)
    LINK_PLAYER_AND_TYPE_PLAYER = {PLAYER_X:None, PLAYER_O:None}

    PLAYER_PEOPLE = ('Человек',)
    PLAYER_BOT    = ('Бот',)

    if   type_of_game == PEOPLE_PEOPLE:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_X] = PLAYER_PEOPLE
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_O] = PLAYER_PEOPLE
    elif type_of_game == PEOPLE_BOT:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_X] = PLAYER_PEOPLE
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_O] = PLAYER_BOT
    elif type_of_game == BOT_BOT:
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_X] = PLAYER_BOT
        LINK_PLAYER_AND_TYPE_PLAYER[PLAYER_O] = PLAYER_BOT

    # игровые символы
    X = 'X'; O = 'O'; P = ' '
    # связка игроков и их типов (человек или бот)
    LINK_PLAYER_AND_SYMBOL = {PLAYER_X:X, PLAYER_O:O}
    #-----------------------------------------

    r = randint(0,len(PLAYERS)-1) # жеребьёвка между всеми игроками
    curr_player = PLAYERS[r] # игрок начинающий игру
    name = f'{curr_player[0]} ({LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]})'
    print(f'После жеребьёвки первым делает ход {name}')

    number_move = 1 # номер хода
    #-------------------------------------------
    # выигрышные комбинации
    WIN_COMBOS = ({0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}) 
    # выигрышные комбинации для КРЕСТИКА
    win_combos_X = []
    for x in WIN_COMBOS:
        set1 = x.copy()
        win_combos_X.append(set1)    
    # выигрышные комбинации для НОЛИКА
    win_combos_O = []
    for x in WIN_COMBOS:
        set1 = x.copy()
        win_combos_O.append(set1)    

    # рейтинг ячеек
    rating_cell = [3,2,3,2,4,2,3,2,3]
    # возможные ходы; будут уходить из списка
    possible_moves = [i for i in range(9)]
    # состояние игрового поля
    playing_field = [P for _ in range(9)]
    print('Начало игры')
    print_playing_field(playing_field)
    
    winner_symbol = None # победитель

    # главный цикл
    while(number_move <= 9):
        name = curr_player[0]
        if LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_BOT:
           name += ' ('+LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]+')'
        text_bot    = f'Ход {number_move}. {name}.'
        text_people = f'Ход {number_move}. {name} введите номер клетки :'

        # получение данных от человека
        if LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_PEOPLE:
            while(True): # ожидание правильных данных от человека
                n = int(input(text_people))
                if n in possible_moves: break
        # получение данных от бота
        elif LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_BOT:
            n = find_better_move(playing_field, curr_player, PLAYER_X, PLAYER_O
                                 , win_combos_X, win_combos_O,rating_cell, X,O)
            #print('n=',n,'rating_cell=',rating_cell,'win_combos_X=',win_combos_X,'win_combos_O=',win_combos_O)
            print('Бот думает ...')
            sleep(2) # оживить бота  :)
            # старый Вариант №1 - ход по порядку - для подстраховки, чтобы не пугать игрока
            if not n: n = possible_moves[0] 
            print(text_bot)

        # установить соответстсующий символ в игровое поле
        playing_field[n] = LINK_PLAYER_AND_SYMBOL[curr_player]
        print_playing_field(playing_field)
        possible_moves.remove(n) 
        rating_cell[n] = -1 
        # привести в соответствие выгрышные комбинации
        #  (ход КРЕСТИКА изменяет выигрышные комбинации у НОЛИКА и наоборот) 
        if curr_player == PLAYER_X: 
            sets_for_del = []
            for set1 in win_combos_O:
                if n in set1:
                    sets_for_del.append(set1)
            for set1 in sets_for_del:
                win_combos_O.remove(set1)
        elif curr_player == PLAYER_O:
            sets_for_del = []
            for set1 in win_combos_X:
                if n in set1:
                    sets_for_del.append(set1)
            for set1 in sets_for_del:
                win_combos_X.remove(set1)


        number_move += 1  # номер хода увеличить
        if number_move > 4: # раньше нет смысла искать победителя
            winner_symbol = check_win_combo(playing_field, WIN_COMBOS, X,O)
            if winner_symbol: break # победитель определен

        curr_player = PLAYER_X if curr_player == PLAYER_O else PLAYER_O  # смена игрока
    # КОНЕЦ ЦИКЛА   
    #------------------------------------------------------------    
    # для определения игрока, который ходил последним
    print('-'*20)
    if winner_symbol:
        name = curr_player[0]
        if LINK_PLAYER_AND_TYPE_PLAYER[curr_player] == PLAYER_BOT:
           name += ' ('+LINK_PLAYER_AND_TYPE_PLAYER[curr_player][0]+')'
        print(f'{name} выиграл!')
    else: print('Ничья.')
    print('-'*20)
    #--------------
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s and s != '0'
#------






def compression_RLE_without_1(text):
    list1 = []
    qty = 0 # кол-во повторений
    before_letter = text[0] if len(text)>0 else ''
    for letter in text:
        if letter == before_letter: 
            qty += 1
        else:     
            if qty>1: list1.append(str(qty))
            list1.append(before_letter)
            qty = 1 # т.к. одна буква уже найдена
            before_letter = letter
    # сохранение последней последовательности одинаковых символов
    if qty>1: list1.append(str(qty))
    list1.append(before_letter)
    return ''.join(list1)

def decompression_RLE_more_9(text):
    list1 = []
    list_qty = []
    for letter in text:
        if letter.isdigit(): 
            list_qty.append(letter)
        else:
            str_qty = ''.join(list_qty)
            qty = int(''.join(list_qty)) if str_qty else 1
            list1.append(letter * qty)
            list_qty = []
    return ''.join(list1)


taskName = '''Задание  №4. Реализуйте RLE алгоритм: 
реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
           '''
isRepeat = True
while(isRepeat): 
    print("")
    print("")
    print("")
    print("-----------------------------------\n\r"+taskName)
    print("Текст из файла file1.txt")
    text1: str 
    text_compressed: str 
    with open('file1.txt', 'r', encoding='utf-8') as f:
        text1 = f.read()
    print("-"*20)
    print(text1)
    print("-"*20)
    text = compression_RLE_without_1(text1)
#    print("Сохранение сжатого текста в file2.txt")
    with open('file2.txt', 'w', encoding='utf-8') as f:
        f.write(text)
#    print("-"*20)
#    print(text)
#    print("-"*20)
    print("Сжатый текст из файла file2.txt")
    with open('file2.txt', 'r', encoding='utf-8') as f:
        text_compressed = f.read()
    print("-"*20)
    print(text_compressed)
    print("-"*20)
    print("Текст восстановлен.")
    text = decompression_RLE_more_9(text_compressed)
    print("-"*20)
    print(text)
    print("-"*20)
    if (text1 == text): 
        print("Совпадают начальный и конечный тексты.") 
        print(" "*5,f"{int(100.0 * len(text_compressed) / len(text1))}% - объем сжатого текста относительно исходного")
    else:     
        print("Не совпадают начальный и конечный тексты.") 
    #--------------
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s and s != '0'
#------






