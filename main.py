from functions import *

print(Fore.MAGENTA+"WELCOME TO GENERAL SCIENCE QUIZ GAME!")
print(Fore.CYAN+"\n(1)New Game\n(2)Exit\n")
x = input("Please choose an option: ")

if x != "1" and x != "2":
    print(Fore.RED+"ERROR!")
    x = input("Please enter 1 or 2: ")
if x == "1":
    new_game()
    while play_again():
        new_game()
elif x == "2":
    exit()
