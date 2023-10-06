def MultiByFive(x, y, z):
    print(x, "+", y, "+", z, "is", x+y+z)
    
    
MultiByFive(3,5,7)



from winsound import Beep

def StarWarsBeep():   
    Beep(440, 500)
    Beep(440, 500)
    Beep(440, 500)
    Beep(349, 350)
    Beep(523, 150)
   
StarWarsBeep()

import random

def itemdropper():
    num = random.randrange (0,100)
    if num <20:
        print ("You got a potion!")
    elif num <50:
        print ("You got a cupcake!")
    elif num <75:
        print ("You got a dirty sock!")
    elif num <100:
        print ("You got nothing!")
    else:
        print("Nothing is here")

while True:
   itemdropper()
   choice = input("Enter any key to continue....")
   
