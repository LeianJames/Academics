def calculate_answer(x, y, operator):

    if operator == "+":
        answer = x + y
    elif operator == "-":
        answer = x - y
    elif operator == "*":
        answer = x * y
    elif operator == "/":
        answer = x / y
    
    return answer
