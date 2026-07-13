number1 = float(input("First number: "))
number2 = float(input("Second number: "))
valid_operation = False 

operation = input("Operation: ")
if operation == "+":
    valid_operation = True
    answer = number1 + number2 


elif operation == "-":
    valid_operation = True
    answer = number1 - number2

elif operation == "*":
    valid_operation = True
    answer = number1 * number2

elif operation == "/":
    valid_operation = True
    answer = number1 / number2

else:
    print ("Invalid operation")
    
if valid_operation:
    print(answer)

 
