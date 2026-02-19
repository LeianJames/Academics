from colorama import init, Fore , Style, Back
from art import tprint, text2art, aprint
import pyinputplus as py

init(autoreset=True)

print (text2art("Welcome"))
pasado = "Passed"
failed = "Failed"
grade = (py.inputInt("Enter grade: "))

if grade >= 75:
    print("Final Grade: ", Fore.GREEN + pasado)
    
    choice = py.inputChoice(['red','blue','yellow'])
    red = text2art("RED")
    blue = text2art("blue")
    yellow = text2art("yellow")

    if choice == 'red':
        print(Fore.RED + red)
    elif choice == 'blue':
        print(Fore.BLUE + blue )
    elif choice == 'yellow':
        print(Fore.YELLOW + yellow )

elif grade <= 74:
    print("Final Grade: ", Fore.RED + failed)