# # 38. Напишите программу, удаляющую из 
# # текста все слова содержащие "абв".
# # ++++++
# # ++++++
# # ++++++
# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)

# # _________________________________

# file5 = open('file5.txt', 'w')
# ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
# file5.write(ex5)
# file5.close()


# def coding(txt):
#      count = 1
#      res = ''
#      for i in range(len(txt)-1):
#          if txt[i] == txt[i+1]:
#              count += 1
#          else:
#              res = res + str(count) + txt[i]
#              count = 1
#      if count > 1 or (txt[len(txt)-2] != txt[-1]):
#          res = res + str(count) + txt[-1]
#      return res

# def decoding(txt):
#      num = ''
#      res = ''
#      for i in range(len(txt)):
#          if not txt[i].isalpha():
#              num += txt[i]
#          else:
#              res = res + txt[i] * int(num)
#              num = ''
#      return res

#  pol6 = open('file6.txt', 'w')
#  coding (ex5)
#  pol6.write(coding(ex5))

#  print(coding(ex5))
#  print(decoding(coding(ex5)))
#  pol6.close()






# ________________________________

# print()
# print('1.Задача: Удалить из текста все слова, содержащие ""абв""')
# with open('text.txt', 'r', encoding = 'utf_8') as data:
#     stroka = data.read().split()
# print(f'В файле записано: {stroka}')
# print('Удалили все слова с абв и получили: ')
# print(' '.join([word for word in stroka if 'абв' not in word]))
# print()

# ________________________________
# text = 'Вот текст в абвтап котором абвабвабв нужно абвктн удалить все абвгод слова, абвнт содержащие определенное сочетание  "абв"'

#  def udalenie_slov(text):
#      text = list(filter(lambda x: 'абв' not in x, text.split()))
#      return " ".join(text)

#  text = udalenie_slov(text)
#  print(text)



# 2. Игра с кончетами. Дано N конфет.
# # Каждый игрок за каждый ход может взять не более M конфет.
# # Побеждает игрок,забравший последнюю конфету.

# # +++++
# # +++++
# # +++++


# from random import randint

# a = int(input('Введите количество конфет'))
# hod = 0
# wins = {0: 'Игрок', 1: 'Бот'}
# while a > 0:
#     if a <= 28:
#         print(f'Выиграл {wins[hod]}')
#         break
#     if hod % 2 == 0:
#         print('Ход Игрока')
#         d = int(input('Введите количество конфет, которое хотите взять'))
#         a -= d
#         print(f'Осталось конфет: {a}')
#     else:
#         print('Ход Бота')
#         d = a % 29
#         a -= d
#         print(f'Осталось конфет: {a}')
#     hod = (hod + 1) % 2







# # man vs smart bot
# ???????????????????????
# from os import system
# system("cls")
# import random

# def get_number(input_string:str)->int:
#     '''
#     Получение количества конфет
#     '''
#     while True:
#         try:
#             num = int(input(input_string))
#             if 0 < num < 29:
#                 return num
#             else:
#                 print('Неправильно. Давай еще раз.')
#         except ValueError:
#             print('Это не то ...')

# def last_move(input_string:str, number:int)->int:
#     '''
#     Получение количества конфет
#     для последнего хода
#     '''
#     while True:
#         try:
#             num = int(input(input_string))
#             if 0 < num <= number:
#                 return num
#             else:
#                 print('Неправильно. Давай еще раз.')
#         except ValueError:
#             print('Это не то ...')

# def get_player(player_0:str, player_1:str)->str:
#     '''
#     Получение имени игроков
#     определение первого хода
#     '''
#     print('Сейчас мы разыграем право первого хода...')
#     temp = random.randint(0, 1)
#     if temp == 0:
#         gamer = player_0
#     else:
#         gamer = player_1
#     print(f'И первым у нас берет конфеты {gamer}!')
#     return gamer

# def playng(candy:int, player:str, player_1:str, player_2:str)->str:
#     winner = ''
#     while candy > 0:
#         if candy > 28:
#             if player == player_1:
#                 print(f'У нас {candy} конфет.')
#                 move = get_number(f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
#                 candy -= move
#                 player = player_2
#                 winner = player_1
#             else:
#                 print(f'У нас {candy} конфет.')
#                 move = get_number(f'{player} сколько вы берете кофет? Вы можете взять от 1 до 28: ')
#                 candy -= move
#                 player = player_1
#                 winner = player_2
#         else:
#             if player == player_1:
#                 print(f'У нас {candy} конфет.')
#                 move = last_move(f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
#                 candy -= move
#                 player = player_2
#                 winner = player_1
#             else:
#                 print(f'У нас {candy} конфет.')
#                 move = last_move(f'{player} сколько вы берете кофет? Вы можете взять от 1 до {candy}: ', candy)
#                 candy -= move
#                 player = player_1
#                 winner = player_2
#     return winner


# print('''
# Добро пожаловать в игру "Sweet Life".
# Правила нашей игры:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Выигрывает игрок сделавший последний ход 
# - он забирает все конфеты.\n''')

# name_0 = input('''Давайте знакомиться. Первый игрок, как к Вам обращаться?\n''')
# name_1 = input('Второй игрок, представтесь, пожалуйста:\n')
# gamer = get_player(name_0, name_1)
# sweet = 2021
# winner = playng(sweet, gamer, name_0, name_1)
# print(f'''
# У нас есть победитель.
# Это {winner}!!!
# Наша игра закончена.''') 

# ________________________________

# from random import randint, choice

# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся. '
#             'Итак, начнём!')

# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# def introduce_players():
#     player1 = input('Давайте познакомися. Как Вас зовут?\n')
#     player2 = 'Робик'
#     print(f'Очень приятно, меня зовут {player2}')
#     return [player1, player2]


# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать?\n '))
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = int(input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [n, m, int(first)]


# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % rules[1] + 1
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(
#                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]


# print(greeting)

# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# # _____________________________________-

# from random import randint

#  def nachalo(name):
#    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#    return x

#  def xod_igroka(name, n, count, m):
#      print(f"Ход {name}, он(а) взял(а) {n} конфет, теперь у {name} {count} конфет. На столе осталось {m} конфет.")

#  igrok1 = input("Первый игрок введите свое имя: ")
#  igrok2 = input("Второй игрок введите свое имя: ")
#  m = int(input("Введите количество конфет на столе: "))
#  ochered = randint(0,2) 
#  if ochered:
#      print(f"Начинает играть {igrok1}")
#  else:
#      print(f"Начинает играть {igrok2}")

#  count1 = 0 
#  count2 = 0

#  while m > 28:
#      if ochered:
#          n = nachalo(igrok1)
#          count1 += n
#          m -= n
#          ochered = False
#          xod_igroka(igrok1, n, count1, m)
#      else:
#          n = nachalo(igrok2)
#          count2 += n
#          m -= n
#          ochered = True
#          xod_igroka(igrok2, n, count2, m)

#  if ochered:
#      print(f"Поздравляем, выиграл(а) {igrok1}")
#  else:
# # _______________________________________________

#  Создайте программу для игры с конфетами человек против человека.
#  #Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#  #Рассмотрим игру против бота.

#  from random import randint

#  def nachalo(name):
#    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#    return x

#  def xod_igroka(name, n, count, m):
#      print(f"Ход {name}, он(а) взял(а) {n} конфет, теперь у {name} {count} конфет. На столе осталось {m} конфет.")

#  igrok1 = input("Игрок введите свое имя: ")
#  igrok2 = "SuperBot"
#  print(f'Очень приятно, сегодня Вы играете с искуственным  {igrok2}')
#  m = int(input("Введите количество конфет на столе: "))
#  ochered = randint(0,2) 
#  if ochered:
#      print(f"Начинает играть {igrok1}")
#  else:
#      print(f"Начинает играть {igrok2}")

#  count1 = 0 
#  count2 = 0

#  while m > 28:
#      if ochered:
#          n = nachalo(igrok1)
#          count1 += n
#          m -= n
#          ochered = False
#          xod_igroka(igrok1, n, count1, m)
#      else:
#          n = randint(1,29)
#          count2 += n
#          m -= n
#          ochered = True
#          xod_igroka(igrok2, n, count2, m)

#  if ochered:
#      print(f"Поздравляем, выиграл(а) {igrok1}")
#  else:
#      print(f"Поздравляем, выиграл(а) {igrok2}")

# # _______________________________________
#  Создайте программу для игры с конфетами человек против человека.
#  #Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#  # Подумайте как наделить бота ""интеллектом""

#  from random import randint

#  def nachalo(name):
#    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#    return x

#  def xod_igroka(name, n, count, m):
#      print(f"Ход {name}, он(а) взял(а) {n} конфет, теперь у {name} {count} конфет. На столе осталось {m} конфет.")

#  def hod_SuperBot(m):
#      n = randint(1,29)
#      while m-n <= 28 and m > 29:
#          n = randint(1,29)
#      return n


#  igrok1 = input("Игрок введите свое имя: ")
#  igrok2 = "SuperBot"
#  print(f'Очень приятно, сегодня Вы играете с искуственным  {igrok2}')
#  m = int(input("Введите количество конфет на столе: "))
#  ochered = randint(0,2) 
#  if ochered:
#      print(f"Начинает играть {igrok1}")
#  else:
#      print(f"Начинает играть {igrok2}")

#  count1 = 0 
#  count2 = 0
#  count = 0
#  countb = 0
#  sumcount = 0

#  while m > 28:
#      if ochered:
#          n = nachalo(igrok1)
#          count1 += n
#          m -= n
#          count +=1
#          ochered = False
#          xod_igroka(igrok1, n, count1, m)
#          print(f"SuperBot считает шаги, {igrok1} Это ваша попытка номер {count}")
#      else:
#          n = hod_SuperBot(m)
#          count2 += n
#          m -= n
#          countb +=1
#          ochered = True
#          xod_igroka(igrok2, n, count2, m)
#          print(f"У SuperBot это  попытка номер {countb}")
#  sumcount = count + countb


#  if ochered:
#      print(f"Поздравляем, выиграл(а) {igrok1}")
#  else:
#      print(f"Поздравляем, выиграл(а) {igrok2}")
#  print (f"Общее число ходов {sumcount}")

# ------------------------------------------





# 3. Создайте программу для игры в ""Крестики-нолики"".
# import random
# import os

# def print_array(field):   #игровое поле крестиков-ноликов
#     os.system('cls')
#     for i in range(1, 10):
#         print(f"{field[i - 1]} ", end="")
#         if not i%3: print()

# def filling(array, array_ex, set): 
#     x = int(input("Выберете клетку: "))
#     if x in array_ex:
#         for i in range(len(array)):
#             if array[i] == x:
#                 if set: array[i] = "X"
#                 else: array[i] = "O"
#         array_ex.remove(x)
#     else:
#         print("Поле занято, или вы вышли за границы игрового поля")
#         filling(array, array_ex, set)


# def win_set(array): 
#     if (array[0] == array[1] == array[2] or
#      array[3] == array[4] == array[5] or
#      array[6] == array[7] == array[8] or
#      array[0] == array[3] == array[6] or
#      array[1] == array[4] == array[7] or
#      array[2] == array[5] == array[8] or
#      array[0] == array[4] == array[8] or
#      array[2] == array[4] == array[6]) :
#         return True
#     else:
#         return False


# def play(array, array_ex, set):  
#     print_array(array)
#     if array_ex == []:
#         print("Победила Дружба!")
#         return

#     if set:
#         player = "1-й"
#     else: 
#         player = '2-й'
#     print(f"Ходит {player} игрок")

#     filling(array, array_ex, set)

#     if win_set(array):
#         print_array(array)
#         print(f"Выиграл {player} игрок \n GAME OVER")
#         return
#     play(array, array_ex, not set)

# field = [int(i) for i in range(1, 10)]      
# field_ex = [int(i) for i in range(1, 10)] 

# set = random.randint(0,1)
# play(field, field_ex, set)


# пайгейм
# # # ++++++++++++
# # # ++++++++++++
# # # ++++++++++++

# import pygame
# import sys

# def check_win(mas,sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return f'{sign} wins!'
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return f'{sign} wins!'
#         if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
#             return f'{sign} wins!'
#         if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
#             return f'{sign} wins!'
#         if zeroes == 0:
#             return 'Peace :)'
#         return False

# pygame.init()
# size_block = 100
# margin = 15
# width = height = size_block*3 + margin*4

# size_window = (width, height)
# screen = pygame.display.set_mode(size_window)
# pygame.display.set_caption("Крестики-нолики")

# black = (60, 60, 60)
# red = (255, 99, 71)
# green = (60, 179, 113)
# white = (240, 240, 240)
# yellow = (255, 165, 0)
# mas = [[0]*3 for i in range(3)] # массив из 9 пустых клеток
# query = 0 # очередность хода
# game_over = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col = x_mouse // (size_block + margin)
#             row = y_mouse // (size_block + margin)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query+= 1
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # перезапуск игры при нажатии пробела
#             game_over = False
#             mas = [[0]*3 for i in range(3)]
#             query = 0
#             screen.fill(black)
#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col*size_block + (col+1)*margin
#                 y = row*size_block + (row+1)*margin
#                 pygame.draw.rect(screen, color, (x,y,size_block,size_block))
#                 if color == red:
#                     pygame.draw.line(screen,white,(x+5,y+5), (x+size_block-5, y+size_block-5),6)
#                     pygame.draw.line(screen,white,(x+size_block-5,y+5), (x+5, y+size_block-5),6)
#                 elif color == green:
#                     pygame.draw.circle(screen,white,(x+size_block//2, y+size_block//2), size_block//2 - 3, 4)
#     if (query-1)%2 == 0:
#         game_over = check_win(mas,'x')
#     else:
#         game_over = check_win(mas,'o')

#     if game_over:
#         screen.fill(black)
#         font = pygame.font.SysFont('peachyday', 80)
#         text1 = font.render(game_over, True, yellow)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width() / 2 - text_rect.width / 2
#         text_y = screen.get_height() / 2 - text_rect.height / 2
#         screen.blit(text1, [text_x, text_y])

#     pygame.display.update()

# # ___________________________________

# Создайте программу для игры в ""Крестики-нолики"".
# # # # # # # +++++++++++++++++++++++++++++++++
# # +++++++++
# # +++++++

#  doska = list(range(1,10))

#  def draw_board(board):

#      for i in range(3):
#          print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")

#  def stavim_hod(hod):
#      valid = False
#      while not valid:
#          otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
#          otv = int(otvet)
#          if otv >= 1 and otv <= 9:
#              if (str(doska[otv-1]) not in "XO"):
#                  doska[otv-1] = hod
#                  valid = True
#              else:
#                  print ("Эта клетка занята")

#  def kto_viigral(doska):
#      pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#      for x in pobeda:
#          if doska[x[0]] == doska[x[1]] == doska[x[2]]:
#              return doska[x[0]]
#      return False

#  def igra(doska):
#      count = 0
#      win = False
#      while not win:
#          draw_board(doska)
#          if count % 2 == 0:
#              stavim_hod("X")
#          else:
#              stavim_hod("O")
#          count += 1
#          if count > 4:
#              m = kto_viigral(doska)
#              if m:
#                  print (m, "Победил!")
#                  win = True
#                  break
#          if count == 9:
#              print ("Победила дружба!")
#              break
#      draw_board(doska)

#  igra(doska)




# 4.Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#     # - входные и выходные данные хранятся в отдельных файлах


# ++++
# ++++
# ++++

# #Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# def Compression(text): #алгоритм сжатия
#     compresdata = ''

#     i = 0
#     while i < len(text):
#         count = 1
#         while i + 1 < len(text) and text[i] == text[i + 1]:
#             count += 1
#             i += 1
#         compresdata += str(count) + text[i]
#         i += 1
    
#     return compresdata


# def Recovery(text): #алгоритм восстановления
#     datarecovery = ''

#     i = 0
#     while i < len(text):
#         datarecovery += str(text[i+1]) * int(text[i])
#         i+=2
    
#     return datarecovery


# with open('Text1.txt', 'r') as t1:
#     t1 = t1.read()    

# with open('Text2.txt', 'w+') as t2:
#     t2.write(Compression(t1))
#     t2.seek(0)                     #возврат курсора на начало строки
#     t2 = t2.read()
 
# with open('Text3.txt', 'w') as t3:
#     t3.write(Recovery(t2))



# # ++++++=
# # +++++++
# # +++++++  
# aaa9999aasss87sslkjhllll -unzip

# 3a492a3s872slkjh4l - zip


#  file5 = open('file5.txt', 'w')
#  ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
#  file5.write(ex5)
#  file5.close()


#  def coding(txt):
#      count = 1
#      res = ''
#      for i in range(len(txt)-1):
#          if txt[i] == txt[i+1]:
#              count += 1
#          else:
#              res = res + str(count) + txt[i]
#              count = 1
#      if count > 1 or (txt[len(txt)-2] != txt[-1]):
#          res = res + str(count) + txt[-1]
#      return res

#  def decoding(txt):
#      num = ''
#      res = ''
#      for i in range(len(txt)):
#          if not txt[i].isalpha():
#              num += txt[i]
#          else:
#              res = res + txt[i] * int(num)
#              num = ''
#      return res

#  pol6 = open('file6.txt', 'w')
#  coding (ex5)
#  pol6.write(coding(ex5))

#  print(coding(ex5))
#  print(decoding(coding(ex5)))
#  pol6.close()


 