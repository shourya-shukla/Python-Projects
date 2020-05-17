import random
print("Welcome to the Stone, Paper, Scissor Game created by Shourya")
a = 8#No. of attempts
print("The choices are :- \nStone => 1\nPaper => 2\nScissor => 3")
ch= (1, 2, 3) #Choices for computer
up = 0 #User points
cp = 0 #Computer points

while(a>0):
     us=int(input ("What is your choice ? \n"))
     cs=random.choice(ch)
     
     if us==1 and cs==1:
         print("Draw")
         a = a - 1
         
     elif us==1 and cs==2:
         cp = cp + 1
         print("You Lose")
         a = a - 1
     
     elif us==1 and cs==3:
         up = up + 1
         print("You Won")
         a = a - 1
         
     elif us==2 and cs==2:
         print("Draw")
         a = a - 1
         
     elif us==2 and cs==3:
         cp = cp + 1
         print("You Lose")
         a = a - 1
     
     elif us==2 and cs==1:
         up = up + 1
         print("You Won")
         a = a - 1
         
     elif us==3 and cs==3:
         print("Draw")
         a = a - 1
         
     elif us==3 and cs==1:
         cp = cp + 1
         print("You Lose")
         a = a - 1
     
     elif us==3 and cs==2:
         up = up + 1
         print("You Won")
         a = a - 1
         
     else :
         print("Invalid Input, Try Again")
         
     print("No. of attempts left = ", a)

else:         
    print("\n\nGame Over\nThe Results are:\nYour Points = ", up, "\nComputer Points = ", cp)

    if up > cp:
        print("Congrats! You Won")

    elif cp > up:
        print("Better Luck Next Time")

    else :
        print("There is a draw")