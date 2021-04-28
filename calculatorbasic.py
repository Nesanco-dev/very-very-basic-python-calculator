selection = input("Python Calculator by Nesanco: Value type: ")
if selection == "addition":
  num1 = input('Enter first number: ')
  num2 = input('Enter second number: ')
  sum = float(num1) + float(num2)
  print('The answer of {0} + {1} is {2}'.format(num1, num2, sum))
if selection == "subtraction":
  num1 = input('Enter first number: ')
  num2 = input('Enter second number: ')
  sum = float(num1) - float(num2)
  print('The answer of {0} - {1} is {2}'.format(num1, num2, sum))
if selection == "multiply":
  num1 = input('Enter first number: ')
  num2 = input('Enter second number: ')
  sum = float(num1) * float(num2)
  print('The answer of {0} x {1} is {2}'.format(num1, num2, sum))
if selection == "divide":
  num1 = input('Enter first number: ')
  num2 = input('Enter second number: ')
  sum = float(num1)/float(num2)
  print('The answer of {0} ÷ {1} is {2}'.format(num1, num2, sum))
if selection != "addition" or "subtraction" or "multiply" or "divide":
  print("Unknown Value, Value Types: subtraction, multiply, divide, addition")