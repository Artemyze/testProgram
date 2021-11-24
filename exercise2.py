import os
def render():
    ph = "*"
    print(ph*5)
    print(ph + " 3 " + ph)
    print(ph*5)
def greet():
    ph = "*"
    print(65*ph)
    print(ph*5+" Здравствуйте! Приветствую вас в игре крестики-нолики! "+ph*5)
    print(ph*4+" В игру играют два игрока, каждый игрок ходит по очереди "+ph*4)
    print(ph*7+" Один игрок управляет крестиком, другой - ноликом "+ph*8)
    print(ph*5+" Поочередно игроки вводят номер ячейки, куда поставить "+ph*5)
    print(ph*9+" свой крестик или же нолик. Победит тот игрок, "+ph*9)
    print(ph + " чьи крестики или нолики займут полностью строку или диагональ " + ph)
    print(65 * ph)
    print(f"{65*'!'}\n{25*'!'} Приятной игры {25*'!'}\n{65*'!'}\n")
    input("Нажмите Enter для продолжения...")
    os.system('clear')

greet()
Field = [i+1 for i in range(9)]
str_arr = ''
for i in range(len(Field)):
    str_arr += str(Field[i])
print(str_arr)
