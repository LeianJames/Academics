import random
import math
import datetime
from operators import calculate_answer

print("Welcome to Math Shuffle Game!! ")

name = str(input("Enter username: "))
start = str(input("Click to Start the Game (Enter 1 to start, 2 to exit): "))

if start == "1":
    print("Game starting... \n")
    
    score = 0
    total_problems = 6
    
    for i in range(1, 7):
        print(f"Question {i} of 6")
        
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        
        operators = ["+", "-", "*", "/"]
        operator = random.choice(operators)
        
        answer = calculate_answer(x, y, operator)               # Calculate answer using the operator function
        
        rounded_answer = round(answer, 2)
        
        print(f"You have 10 seconds to answer...")
    
        start_time = datetime.datetime.now()                    # datetime.datetime.now() - Gets the current date and time as a datetime object
        user_input = input(f"{x} {operator} {y} = ")
        
        
        end_time = datetime.datetime.now()                      # datetime.datetime.now() - Gets the current date and time again to calculate elapsed time
        
        
        elapsed_time = (end_time - start_time).total_seconds()  # .total_seconds() - Converts the time difference to total seconds as a float
        
        if elapsed_time > 10 or user_input.strip() == "":
            print(f"Time expired! The correct answer is {rounded_answer}")
            print(f"Points awarded: 0")
        else:
            try:
                question = float(user_input)
                question_rounded = round(question, 2)
                
                if question_rounded == rounded_answer:
                    print("That's correct!")
                    score += 10
                    print(f"Points awarded: 10")
                else:
                    print(f"Wrong, the correct answer is {rounded_answer}")
                    score += 1
                    print(f"Points awarded: 1")
                    
            except ValueError:
                print("Invalid input! Please enter a number.")
                print(f"The correct answer is {rounded_answer}")
                score += 1
                print(f"Points awarded: 1")
        
        # Automatically proceed to next problem
        if i < 6:
            print("Proceeding to next problem...\n")
        else:
            print()
    
    average_score = math.floor(score / total_problems)
    
    print("=" * 40)
    print(f"Player Name: {name}")
    print(f"Total Score: {score}")
    print(f"Average Score: {average_score}")
    print("=" * 40)
    
else:
    print("Exiting program...")
