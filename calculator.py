'''
Here we have created a mini-project for python beginners.In this
Mini-projectwe have created a calculator to perform basic 
calculations like Addition, Subtraction, Multiplication, Division

'''


#Taking input for first number and second number from user to perform calculations
a = input("Enter first number:  ")
a = int(a)
b = input("Enter second number:  ")
b = int(b)

#Now we are defining different functions to perform different calculations 
#Here we have defined functions to Add, Subtract, Multiply and Divide
def Add(num1, num2):
    print("Your result is: ", num1+num2)

def Subtract(num1, num2):
    print("Your result is: ", num1-num2)

def Multiply(num1, num2):
    print("Your result is: ", num1*num2)

def Divide(num1, num2):
    print("Your result is: ", num1/num2)


# Giving user prompt 
# Here in prompt we have given a multiline string not a  multiline comment
# Here we will add a while loop so that the program continues
while (True):
    prompt = '''
    Enter 0 for Addition, 1 for Substraction, 
    2 for Multiplication, 3 for Division
    '''
    print(prompt)

    # Taking input from user to perform task
    userInput = input()
    userInput = int(userInput)


    # Here we have created a if-else ladder to perform different calculations
    # It will perform calculations according to what userinput() user has given by seeing the prompt
    # And if user will input any other number that is not given in prompt it will show "Invalid input"
    if(userInput == 0):
        print("Adding these numbers.....")
        Add(a, b)
    elif(userInput == 1):
        print("Subtracting these numbers.....")
        Subtract(a, b)
    elif(userInput == 3):
        print("Multiplying these numbers.....")
        Multiply(a, b)
    elif(userInput == 3):
        print("dividing these numbers.....")
        Divide(a, b)
    else:
        print("Invalid input")
        print("Enter any of the folowing")
        print(prompt)
        
      
