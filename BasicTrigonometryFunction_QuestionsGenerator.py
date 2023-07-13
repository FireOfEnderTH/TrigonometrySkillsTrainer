#YOU CAN ADD EVEN MORE EXPRESsIONS, ANGLES, OR TRIGONOMETRY FUNCTIONS AS YOU DESIRED

from math import sin,cos,tan,sqrt,radians #import math library for calculation
from random import randint #import randint to random the questions
from colorama import Fore, init #import colorama to colorize the texts
init(convert=True,autoreset=True) #make colorama functionable and reset text color when print new texts
print(Fore.LIGHTGREEN_EX + "\n  LET TRAIN YOUR TRIGONOMETRY SKILL!\n") #print the header

angles = [0,30,37,45,53,60,90] #angles to be use in the questions
shifting = [0,0,0,0,0,0,-360,-270,-180,-90,90,180,270] #angles to be added to an angles for even more difficulty
#many 0s to increase the chance for them to get chose

#define list of strings those can be use to refer to square root (sqrt)
syntax_for_sqrt = ['root','rt','sq','sqr','sqt','root','√','square','squareroot','square root','รูท','ราก','รูต','รูด','รากที่สอง','รากที่สองของ']

#define responses for different situation
correct_response = "  YES, YOU'RE RIGHT!\n"
wrong_response = "  INCORRECT, TRY AGAIN.\n  (please answer in number with decimals or 'inf' or 'unidentified' or empty set or fraction form)\n"
typeError_response = "  YOU TYPED SOMETHING WRONG!\n"
skip_response = "FINE, LET SKIP.\n"

def skip(): #player skips the question
    print(Fore.WHITE + skip_response)

def submit(text): #player answers the question
    if text.lower() == 'skip' or text.lower() == 'sk' or text.lower() == 'skp': #allow to use various expressions for skipping
        skip()
    elif text.lower() == 'exit' or text.lower() == 'stop' or text.lower() == 'end': #allow to use various expressions exiting
        exit()
    else: #didn't skip or exit
        for t in syntax_for_sqrt: #change any text that refers to square root to sqrt for calculation
            if text.lower().replace(f'{t}(','sqrt(').count('sqrt') > text.count('sqrt'): #if the text length is lesser or equal the same one, it has a possibility to be error replacing
                text = text.lower().replace(f'{t}(','sqrt(') #replace the text with sqrt(    *so players need to type brackets to correctly answer the question
        
        if ans == 'inf': #it's tan(0°) which is either infinity or unidentified regards to the case.
            #allow to use various answers to answer this question
            if text.lower() == ans or text.lower() == 'infinity' or text.lower() == 'อนันต์' or text.lower() == '∞' or text.lower() == 'unidentified' or text.lower() == 'หาค่าไม่ได้' or text.lower() == 'non' or text.lower() == 'nan' or text.lower() == 'non' or text.lower() == '∅' or text.lower() == 'null' or text.lower() == '-' or text.lower() == '{}' or text.lower() == 'huge':
                print(Fore.LIGHTGREEN_EX + correct_response) #correct answer
            else:
                print(Fore.LIGHTRED_EX + wrong_response) #wrong answer
        else:
            try: #use 'try' to catch errors, so the program won't crash or stop
                if round(eval(text),1) == round(ans,1): #use only 1-digit decimals to compare the answer because 'ans' has to many decimals and could make too much different from what players answered
                    print(Fore.LIGHTGREEN_EX + correct_response) #correct answer
                else:
                    print(Fore.LIGHTRED_EX + wrong_response) #wrong answer
            except: #catched the error
                print(Fore.LIGHTYELLOW_EX + typeError_response)

while True: #main loop for the program to run until it exits
    chosen_ang = angles[randint(0,len(angles)-1)] #random angles from the list
    chosen_ang += shifting[randint(0,len(shifting)-1)] #random angles to be added to the chosen angle
    ans = 0 #define a variable to store the correct answer of the question

    #choose trigonometry function to use in the quesion
    k = randint(1,3) #choose a function randomly (1: sin, 2: cos, 3: tan)
    f = '' #define a variale to store the string version of chosen trigonometry function

    if k==1:
        ans = sin(radians(chosen_ang))
        f = 'sin'
    elif k==2:
        ans = cos(radians(chosen_ang))
        f = 'cos'
    else:
        ans = tan(radians(chosen_ang))
        if chosen_ang%180 == 90: #if it's either 90 or 270 (or even 450), make the answer 'inf' instead of 'estimation of infinity' which will lead to unanswerable question
            ans = 'inf'
        f = 'tan'

    #call both answer checking and input functions at once
    submit(input(f'  {f}({chosen_ang}°) = {Fore.LIGHTMAGENTA_EX}?\n  {Fore.WHITE}> {Fore.LIGHTCYAN_EX}'))