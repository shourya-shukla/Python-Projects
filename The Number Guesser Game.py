# Created for fun by: Shourya Shukla
# For more such projects, please do visit https://github.com/shourya-shukla

from random import randrange  # Module to get a random number which is to be guessed

name = input("Please enter your name: ")
print(f"Hello \"{name}\", Welcome to the number guessing game, brought to you by Shourya Shukla.\n")  # Welcome message
d = int(input('''Select Difficulty:
1-Easy
2-Medium
3-Hard
==> '''))  # Select difficulty
if d == 1:  # Easy mode
    num = randrange(1, 10)
    mode = "Easy"
elif d == 2:  # Medium mode
    num = randrange(1, 100)
    mode = "Medium"
elif d == 3:  # Hard mode
    num = randrange(1, 1000)
    mode = "Hard"
else:  # Error
    print("Invalid input")
    exit()
tries = 1
unum = int(input("Okay!, let's start, guess a number: "))
while unum != num:
    if unum > num:  # If entered a larger number
        unum = int(input("Please input a smaller number: "))
    else:  # If entered a smaller number
        unum = int(input("Please input a larger number: "))
    tries = tries + 1
else:
    print("\nCongrats ! You've won the game.")  # Winning message
    print(f"No. of tries: {tries}")  # Tries counter
f = open("leaderboard.txt", "a")
f.write(name+"|"+str(tries)+"|"+mode+"\n")  # Writing scores for leaderboard
f.close()
prompt = input("Do you want to see the leaderboard ?\n==> ")
if prompt == "Yes":
    f = open("leaderboard.txt")
    print(f.read())  # Show leaderboard
    f.close()
elif prompt == "No":
    exit()
else:
    print("Please enter Yes or No.")
