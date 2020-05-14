n = 18 #You can enter number of your choice here
g = 10 #The number of guesses
print("Welcome to the number guesser game, Created by Shourya")
while(g>0):
   inp = int(input("Guess a number\n"))
   if inp>n:
      print("The number is smaller than "+str(inp))
      g = g-1
      print("No. of guesses left = "+str(g))
   elif inp<n:
      print("The number is larger than "+str(inp))
      g = g-1
      print("No. of guesses left = "+str(g))
   else:
      print("Congrats! You Won the Game")
      break
else:
   print("Game Over, Better Luck Next Time")