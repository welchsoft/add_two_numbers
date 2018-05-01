#define function that adds 2 numbers
def addNumbers(num1, num2):
    return num1 + num2

#take the user input
number1 = float(input('enter first number '))
number2 = float(input('enter second number '))
#call the function and print
print("the total is " + str(addNumbers(number1,number2)))
