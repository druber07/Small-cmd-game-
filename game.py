import random
import time
import os
import keyboard

gameRun = 0
#Map generation
map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
lastL = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mapCreator = 0
#Colsole resetor
clear = lambda: os.system('cls')
clear()
#Playe's info
PlayerX = 15
PlayerY = 5

#Builds the map
def mapBuilder():
    global mapCreator, lastL
    if(mapCreator == 0):
        for r in range(30):
            lastL[r] = random.randrange(2)
        mapCreator = 1

    for r in range(9):
        for c in range(30):
            map[r][c] = ' '

    for c in range(30):
        if(lastL[c] == 0):
            map[8][c] = ' '
        else:
            map[8][c] = '_'
    for c in range(30):
        if(lastL[c] == 0):
            map[9][c] = '━'
        else:
            map[9][c] = ' '

def player():
    global PlayerX,PlayerY
    map[PlayerY][PlayerX] = 'P'
    #Gravity
    if(map[PlayerY + 1][PlayerX] != '━' and map[PlayerY+1][PlayerX] != '_'):
        map[PlayerY][PlayerX] = ' '
        PlayerY = PlayerY + 1
        map[PlayerY][PlayerX] = 'P'
def mapRuner(): 
    for r in range(10):
        for c in range(30):
            print(map[r][c],end='')
        print('')


def __main__():
    global PlayerX,PlayerY
    print('Welcome')
    mapBuilder()
    time.sleep(2)
    clear()
    while(gameRun == 0):
        player()
        mapRuner()
        time.sleep(50 / 1000)
        clear()
        while True:
            try:
                if keyboard.is_pressed('w') and PlayerY <= 8:
                    map[PlayerY][PlayerX] = ' '
                    PlayerY = PlayerY - 2
                break
            except:
                break
        while True:
            try:
                if keyboard.is_pressed('d') and map[PlayerY][PlayerX +1] != '━' and map[PlayerY][PlayerX +1 ] != '_':
                    map[PlayerY][PlayerX] = ' '
                    PlayerX = PlayerX + 1
                break
            except:
                break
        while True:
            try:
                if keyboard.is_pressed('a') and map[PlayerY][PlayerX -1 ] != '━' and map[PlayerY][PlayerX -1 ] != '_':
                    map[PlayerY][PlayerX] = ' '
                    PlayerX = PlayerX - 1
                break
            except:
                break
__main__()