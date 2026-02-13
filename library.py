import random
import datetime
import math
import time

try:
    import msvcrt
    _HAS_MS = True
except Exception:
    _HAS_MS = False


def program_start(start):
    if start == "1":
        print("Get Ready!!")
        time.sleep(2)                                               #load the program for 2 seconds
        
        operations = ["+", "-", "*", "/"]
        
        def timed_input(prompt, timeout):
            if not _HAS_MS:
                print(f"You have {timeout} seconds to answer.")
                try:
                    return input(prompt)
                except Exception:
                    return None

            print(prompt, end="", flush=True)
            buf = ""
            start_time = time.time()
            last_remaining = -1
            while True:
                elapsed = time.time() - start_time
                remaining = int(timeout - elapsed)
                if remaining != last_remaining:
                    print(f"\rTime left: {remaining:2d}s ", end="", flush=True)
                    last_remaining = remaining
                if remaining < 0:
                    print()
                    return None
                while msvcrt.kbhit():
                    ch = msvcrt.getwch()
                    if ch in ('\r', '\n'):
                        print()
                        return buf
                    elif ch == '\x08':
                        buf = buf[:-1]
                        print('\b \b', end='', flush=True)
                    else:
                        buf += ch
                        print(ch, end='', flush=True)
                time.sleep(0.05)

        for i in range(6):                      
            x = random.randint(1,20)
            y = random.randint(1,20)
            op = random.choice(operations)

            print(f"\nProblem {i+1}: {x} {op} {y} = ")

            # allow the user to type an answer with a 10-second timer
            user_input = timed_input("Your answer: ", 10)

            # compute correct answer
            if op == "+":
                correct = x + y
            elif op == "-":
                correct = x - y
            elif op == "*":
                correct = x * y
            else:
                correct = x / y

            if user_input is None or user_input.strip() == "":
                print(f"Time's up! The correct answer was {correct:.2f}" if op == "/" else f"Time's up! The correct answer was {correct}")
                continue

            try:
                user_val = float(user_input)
            except ValueError:
                print(f"Invalid answer. The correct answer was {correct:.2f}" if op == "/" else f"Invalid answer. The correct answer was {correct}")
                continue

            # check answer (allow small tolerance for division)
            if op == "/":
                if abs(user_val - correct) <= 0.01:
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer was {correct:.2f}")
            else:
                if abs(user_val - correct) < 1e-6:
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer was {correct}")











def program_exit(start):
    if start =="2":
        print("😢 Exiting Program... ")
