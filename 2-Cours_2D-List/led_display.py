from array_to_led import *

array = [[N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,N,N,B,B,B,N,N,N,N,N,G,G,G,G,G,G,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,N,B,N,N,N,B,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,G,G,G,G,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,B,N,N,N,N,N,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,N,B,N,N,N,B,N,N,N,N,G,N,N,N,N,N,N,N,N,N],
         [N,N,N,R,N,N,N,N,N,N,N,N,B,B,B,N,N,N,N,N,G,G,G,G,G,G,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N],
         [N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N]]

myLed = ArrayLED(array)
while True:
    for i in range(myLed.width) :
        myLed.array[i%20] = myLed.array[(i-1)%20]
    myLed.update()
    #time.sleep(1)
    