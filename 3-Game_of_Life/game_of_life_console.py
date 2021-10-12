from arrayConsole import *

array = [[N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,B,B,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,B,B,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],fhngtuj
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N]]

myLed = ArrayConsole(array)

def update_life():
    next = [[0 for x in range(myLed.width)] for y in range(myLed.height)] 
    for i in range(myLed.width):
        for j in range(myLed.height):
            neighbors = count_neighbors(i,j)

            if (myLed.array[i][j] == 0 and neighbors == 3):
                next[i][j] = 1
            elif (myLed.array[i][j] == 1 and (neighbors < 2 or neighbors > 3)) :
                next[i][j] = 0
            else:
                next[i][j] = myLed.array[i][j]
    myLed.array = next

def count_neighbors(x,y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            myLed.width = (x + i + myLed.width) % myLed.width
            myLed.height = (y + j + myLed.height) % myLed.height
            sum += myLed.array[myLed.width][myLed.height]
    sum -= myLed.array[x][y]
    return sum

while True:
    update_life()    
    myLed.update()