import random
u=input("your turn stone:s ,paper:p,sizer:z\n")
print("its computer's turn")
rand=random.randint(1,3)
if(rand == 1):
    comp= "s"
    print("computer choos stone")
elif rand==2:
    comp="p"
    print("computer choos paper")
elif rand==3:
    comp="z"
    print("computer choos sizer")
def game(comp,u):
    if comp==u:
        return 1
    if comp== "s":
        if u== "p":# win
            return 2
        elif u== "z":# lose
            return 3
    elif comp== "p":
        if u=="z":#win
            return 4
        elif u=="s":#lose
            return 5 
    elif comp=="z":
        if u=="p":
            return 6 # lose
        elif u=="s":
            return 7 # win
g=game(comp,u)
if g==1:
    print("it is a tie")
elif g==2:
    print("you win ")
elif(g==3):
    print("you lose")
elif(g==4):
    print("you win ")
elif(g==5):
    print("you lose")
elif g==6:
    print("you lose")
elif g==7:
    print("you win ")
