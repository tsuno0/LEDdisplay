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
    for i, ligne in enumerate(myLed.array):
        ligne = [ligne[-1]]+ligne[:-1]
        array[i] = ligne
#     new_array = []
#     for ligne in myLed.array:
#         temp_ligne = [None]
#         for i, element in enumerate(ligne):
#             if i < len(ligne)-1:
#                 temp_ligne.append(element)
#             else:
#                 temp_ligne[0] = element
#         new_array.append(temp_ligne)
#     myLed.array = new_array
    
    myLed.update()
    