"""
Improved version of the original calculator program
Areas considered for improvement are highlighted in the IMPROVEMENT file
"""

def operator(sign, num1, num2):
    operators = ['+','-','*','/','pw','=']
    if sign not in operators:
        return "ERROR: 	Operator sign not recognized"
    elif sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1/num2
    elif sign == 'pw':
        return num1 ** num2
    elif sign == '=':
        if num1 == num2:
            return True
        return False
    

print("*" * 80)
user_input = input("Enter operation you would like to calculate (i.e 2 + 2 or 2 * 2)" )
operands = user_input.split()
num1 = float(operands[0])
sign = operands[1]
num2 = float(operands[2])
result = operator(sign, num1, num2)
print(result)
print("*" * 80)
