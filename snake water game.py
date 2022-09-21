import random


def game(USERINPUT , comp):
    if(USERINPUT=='s'):
        if(comp=='w'):
            return True
        elif(comp=='g'):
            return False
        else:
            return 0
    if(USERINPUT=='w'):
        if(comp=='s'):
            return False
        elif(comp=='g'):
            return True
        else:
            return 0
    if(USERINPUT=='g'):
        if(comp=='w'):
            return False
        elif(comp=='s'):
            return True
        else:
            return 0
                


print("WELCOME TO THE GAME OF SNAKE WATER GUN")
USERINPUT =input('''select your option from the below to continue the game :
 snake(s)
 gun(g)
 water(w)
 ''')
print("computer turn : Snake(s) Gun(g) Water(w)")
randno = random.randint(1,3)
if randno==1:
    comp='s'
    print("comp is snake")
elif randno==2:
    comp='g'
    print("comp is gun")
else :
    comp='w'      
    print("comp is water") 
     
print(game(USERINPUT, comp))

gamewin = game(USERINPUT, comp)

if(gamewin== True):
    print("user wins the game")
elif(gamewin== False):
    print("user losses the game")
else:
    print("the match is tied")        