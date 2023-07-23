from numpy import array, linalg #import numpy for matrix works
from random import randint #import randint to random the questions
from colorama import Fore, init #import colorama to colorize the texts
init(convert=True,autoreset=True) #make colorama functionable and reset text color when print new texts
print(Fore.LIGHTGREEN_EX + "\n  LET TRAIN YOUR MATRICES SKILL!\n") #print the header

dimension = 3 #Dimension of the matrix in questions
amp = 15 #Max absolute number to be in the matrices
diff = 7 #Max different number that could help decrease the size of determinant result

#define responses for different situation
correct_response = "  YES, YOU'RE RIGHT! (+1 score)"
wrong_response = "  INCORRECT, TRY AGAIN. (-1 score)\n  CORRECT ANSWER WAS : "
typeError_response = "  YOU TYPED SOMETHING WRONG! (0 score)"
skip_response = "  FINE, LET SKIP. (-1 score)\n"

score = 0 #define variable to contain score for every correct answer and decrease every wrong answer

def printScore(): #just printing the score
    global score #use the same 'score' variable from the global space
    print(Fore.LIGHTYELLOW_EX + f"  Your current score is : {score}\n")

def skip(): #player skips the question
    global score #use the same 'score' variable from the global space
    print(Fore.WHITE + skip_response)
    score -= 1
    printScore()

def generateQuestion(): #generate both questions and answers
    matrix = array([[(randint(0,amp)-randint(0,diff))*[-1,-1,0,1,1][randint(0,4)] for j in range(dimension)] for i in range(dimension)])
    return matrix , int(linalg.det(matrix))

def checkAns(text):
    global score #use the same 'score' variable from the global space
    if text.lower() == 'skip' or text.lower() == 'sk' or text.lower() == 'skp': #allow to use various expressions for skipping
        skip()
    elif text.lower() == 'exit' or text.lower() == 'stop' or text.lower() == 'end': #allow to use various expressions exiting
        exit()
    else: #didn't skip or exit
        try: #use 'try' to catch errors, so the program won't crash or stop
            if eval(text) == a or eval(text) == a+1 or eval(text) == a-1: #use only 1-digit decimals to compare the answer because 'ans' has to many decimals and could make too much different from what players answered
                print(Fore.LIGHTGREEN_EX + correct_response) #correct answer
                score += 1
                printScore()
            else:
                print(Fore.LIGHTRED_EX + wrong_response + str(a)) #wrong answer
                score -= 1
                printScore()
        except: #catched the error
            print(Fore.LIGHTYELLOW_EX + typeError_response)
            printScore()

if __name__ == "__main__":
    while True:
        q,a = generateQuestion() #Get question and answer
        format_str = '{:<5}' #Make it  equally space bar 
        print(f'  Matrix :\n')
        for row in q:
            print(Fore.LIGHTGREEN_EX+'       ' + ''.join(format_str.format(element) for element in row))
        checkAns(input(f'\n{Fore.WHITE}  Determinant {Fore.LIGHTMAGENTA_EX}? {Fore.WHITE}> {Fore.LIGHTCYAN_EX}'))
        