
from colorama import init, Fore, Style, Back
init(autoreset=True)

print(Fore.GREEN + "Hi hello")
print(Style.BRIGHT + "WSUP")
print(Back.BLACK + "Goodbye")

#------------------------------------------------------------------------------------------------------

from art import tprint, text2art, line

tprint("Leian")
tprint("Leian", "block") #u can change block to block, rnd-medium, bubbler, small,

ascii = text2art("Leian")
print(ascii)

ascii = text2art("Leian")
print(Fore.GREEN + ascii)

#------------------------------------------------------------------------------------------------------
'''
import pyinputplus as pyip
num = pyip.inputInt("Enter an integer: ")
test = pyip.inputInt("Enter your age (1-120)", min = 1, max = 120)
zodiac = pyip.inputChoice(["Scorpio", "Capricorn", "Sagittarius"], "Choose your zodiac sign: ")

print(f"num is {num}")
print(f"Zodiac is {zodiac}")

if test <= 18:
    print("Young")
elif test >= 18:
    print("Adult")
'''
#------------------------------------------------------------------------------------------------------
'''
import prettytable

table = prettytable.PrettyTable()

table.field_names = ["FirstName", "Middle", "Surname"]
table.add_row(["Leian", "Perez", "Santos"])
table.add_row(["Lei", "piriz", "suntoes"])

table.align["FirstName"] = 'l'
table.align["Middle"] = 'c'
table.align["Surname"] = 'r'

print(table)
'''
#------------------------------------------------------------------------------------------------------
'''
import pyttsx3 as ts

engine = ts.init()

#engine.setProperty('voice', voice[1]. ID)
engine.say("Hello everyone!")
engine.runAndWait()
'''
#------------------------------------------------------------------------------------------------------
'''
import cowsay

cowsay.cow("Hi")
cowsay.tux("Hello")
cowsay.trex("Hola")
cowsay.dragon("Bonjour")
'''