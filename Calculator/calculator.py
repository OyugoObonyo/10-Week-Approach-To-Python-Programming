"""
A simple calculator
"""

print("+-" * 40)
print ("\t\tA SIMPLE CONSOLE CALCULATOR IMPLEMENTED BY @OyugoObonyo")
print("+-" * 40)
operation = input ("Select desired operation. Multiplication, Division, Addition or Subtraction?")
num1 = input ("First number you would like to operate on?")
num2 = input ("Second number you would like to operate on?")
if operation == "Multiplication":
    try:
        product = float(num1) * float(num2)
        print(product)
    except:
        print("ERROR: OPERATION POSSIBLE ONLY ON NUMBERS")
elif operation == "Division":
    try:
        result = float(num1) / float(num2)
        print(result)
    except:
        print("ERROR: OPERATION POSSIBLE ONLY ON NUMBERS")
elif operation == "Addition":
    try:
        result = float(num1) + float(num2)
        print(result)
    except:
        print("ERROR: OPERATION POSSIBLE ONLY ON NUMBERS")
elif operation == "Subtraction":
    try:
        result = float(num1) - float(num2)
        print(result)
    except:
        print("ERROR: OPERATION POSSIBLE ONLY ON NUMBERS")
