import random
import math
import datetime
import library



name = str(input("Enter username: "))
start = str(input("1 - Start Game \n2 - Exit Program \n"))

if start == "1":
    library.program_start(start)

elif start == "2":
    library.program_exit(start)

else:
    print("Invalid, please try again")