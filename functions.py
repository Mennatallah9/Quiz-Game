questions = {"Brass gets discoloured in air because of the presence of which of the following gases in air?":"b",
"Which of the following is a non metal that remains liquid at room temperature?":"b",
"Chlorophyll is a naturally occurring chelate compound in which central metal is":"b",
"Which of the following is used in pencils?":"a",
"Which of the following metals forms an amalgam with other metals?":"b",
"The gas usually filled in the electric bulb is":"a",
"Washing soda is the common name for":"a",
"Quartz crystals normally used in quartz clocks etc. is chemically":"a",
"Which of the gas is not known as green house gas?":"d",
"Bromine is a":"b",
"The hardest substance available on earth is":"c",
"The variety of coal in which the deposit contains recognisable traces of the original plant material is":"d",
"Tetraethyl lead is used as":"d",
"Which of the following is used as a lubricant?":"a",
"The inert gas which is substituted for nitrogen in the air used by deep sea divers for breathing, is":"c",
"The gases used in different types of welding would include":"d",
"The property of a substance to absorb moisture from the air on exposure is called":"b",
"In which of the following activities silicon carbide is used?":"c",
"The average salinity of sea water is":"b",
"When an iron nail gets rusted, iron oxide is formed":"c"}


options = [["(a)Oxygen", "(b)Hydrogen sulphide", "(c)Carbon dioxide", "(d)Nitrogen"],
["(a)Phosphorous", "(b)Bromine", "(c)Chlorine", "(d)Helium"],
["(a)copper", "(b)magnesium", "(c)iron", "(d)calcium"],
["(a)Graphite", "(b)Silicon", "(c)Charcoal", "(d)Phosphorous"],
["(a)Tin", "(b)Mercury", "(c)Lead", "(d)Zinc"],
["(a)nitrogen", "(b)hydrogen", "(c)carbon dioxide", "(d)oxygen"],
["(a)Sodium carbonate", "(b)Calcium bicarbonate", "(c)Sodium bicarbonate", "(d)Calcium carbonate"],
["(a)silicon dioxide", "(b)germanium oxide", "(c)a mixture of germanium oxide and silicon dioxide", "(d)sodium silicate"],
["(a)Methane", "(b)Nitrous oxide", "(c)Carbon dioxide", "(d)Hydrogen"],
["(a)black solid", "(b)red liquid", "(c)colourless gas", "(d)highly inflammable gas"],
["(a)Gold", "(b)Iron", "(c)Diamond", "(d)Platinum"],
["(a)bitumen", "(b)anthracite", "(c)lignite", "(d)peat"],
["(a)pain killer", "(b)fire extinguisher", "(c)mosquito repellent", "(d)petrol additive"],
["(a)Graphite", "(b)Silica", "(c)Iron Oxide", "(d)Diamond"],
["(a)Argon", "(b)Xenon", "(c)Helium", "(d)Krypton"],
["(a)oxygen and hydrogen", "(b)oxygen, hydrogen, acetylene and nitrogen", "(c)oxygen, acetylene and argon", "(d)oxygen and acetylene"],
["(a)osmosis", "(b)deliquescence", "(c)efflorescence", "(d)desiccation"],
["(a)Making cement and glass", "(b)Disinfecting water of ponds", "(c)cutting very hard substances", "(d)Making casts for statues"],
["(a)3%", "(b)3.5%", "(c)2.5%", "(d)2%"],
["(a)without any change in the weight of the nail", "(b)with decrease in the weight of the nail", "(c)with increase in the weight of the nail", "(d)without any change in colour or weight of the nail"]]

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#--------------------------------------------------------------------------------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------------------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (a, b, c, or d): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#----------------------------------------------------------------------------------------------------------------
def check_answer(answer, guess):

    if answer.upper() == guess:
        print(Fore.GREEN+"CORRECT!", "The answer is:", answer)
        return 1
    else:
        print(Fore.RED+"WRONG!", "The answer is:", answer)
        return 0

#-----------------------------------------------------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------------------------------------------------------------------")
    print("RESULTS")
    print("----------------------------------------------------------------------------------------------------")

    score = int((correct_guesses/len(questions))*100)
    print(Fore.YELLOW+"Your score is: "+str(score)+"%")
#--------------------------------------------------------------------------------------------------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------------------------------
