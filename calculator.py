number1 = float(input("First number: "))
number2 = float(input("Second number: "))

operation = input("Operation: ")
if operation == "+":
    answer = number1 + number2 

elif operation == "-":
    answer = number1 - number2

elif operation == "*":
    answer = number1 * number2

elif operation == "/":
    answer = number1 / number2
    
print(answer)