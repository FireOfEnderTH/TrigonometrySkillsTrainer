from colorama import Fore, init
from random import randint
from ast import literal_eval #The built-in eval() has security risk and calculate varibles such as 'a'
init(convert=True,autoreset=True)
print(Fore.LIGHTGREEN_EX + "\n  LET TRAIN YOUR ARITHMETIC SKILL!\n") 

def askInt(text):
    while True:
        ask = input(f"{Fore.WHITE}  {text}\n  > {Fore.LIGHTCYAN_EX}")
        try:
            ask = int(ask)
            if ask > 0:
                break
            else:
                print(f"{Fore.LIGHTYELLOW_EX}  Please type the {Fore.LIGHTRED_EX}POSITIVE {Fore.LIGHTYELLOW_EX}integer!\n")
        except:
            print(Fore.LIGHTYELLOW_EX + "  Please type the integer!\n")
    print(Fore.LIGHTGREEN_EX + "  OK!\n")
    return ask


if __name__ == "__main__":
    while True:
        amplitude = askInt("What is the range of the integers you desired?")
        min_num = -amplitude
        max_num = amplitude

        min_pile = askInt("Minimum pair(s) of numbers?")
        max_pile = askInt("Maximum pair(s) of numbers?")
        if max_pile < min_pile:
            min_pile = max_pile

        print("\n"*5)

        r = [k for k in range(min_num,max_num+1)]
        r.remove(0)
        score = 0
        restart = False
        while True:
            if restart:
                print("\n"*5)
                break
            q = ""
            a = 0
            for i in range(randint(min_pile, max_pile)):
                    num = [r[randint(0,len(r)-1)] for j in range(2)]
                    if q == "":
                        q += f"({num[0]})({num[1]})"
                        a += (num[0]*num[1])
                    else:
                        symbol = ["+", "-"][randint(0, 1)]
                        q += f" {symbol} ({num[0]})({num[1]})"
                        a += eval(f"{symbol}(({num[0]})*({num[1]}))")

            while True:
                answer = input(f"{Fore.WHITE}  {q}\n  = {Fore.LIGHTCYAN_EX}")
                try:
                    if literal_eval(answer) == a:
                        print(Fore.LIGHTGREEN_EX + "  Correct!")
                        score += 1
                        print(f"{Fore.LIGHTCYAN_EX}  Your score is now : {score}\n")
                        break
                    else:
                        print(f"{Fore.LIGHTRED_EX}  Wrong!\n  The answer was : {Fore.LIGHTYELLOW_EX}{a}")
                        score -= 1
                        print(f"{Fore.LIGHTCYAN_EX}  Your score is now : {score}\n")
                        break
                except:
                    if answer.lower() == "restart" or answer.lower() == "re":
                        restart = True
                        break
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}  Error! Can't recognize the answer\n\n  {Fore.LIGHTCYAN_EX}Try again.")
