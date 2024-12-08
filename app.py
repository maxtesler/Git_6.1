first_num = float(input('Enter your first number: '))

second_num = float(input('Enter your second number: '))

fun = input('Choose +|-|/ function: ')

def num_calc(first_num: float, second_num:float, fun:str):
   if fun == 'add' or fun == '+':
       result = first_num + second_num
   elif fun == 'subtract' or fun == '-':
       result = first_num - second_num
   elif fun == '/':
       result = first_num / second_num
   else: raise ValueError(f"Incorrect function: {fun} .")
  
   print(f'Your result is {result}')

try:
   num_calc(first_num, second_num,fun)
except ValueError as e:
   print(e)