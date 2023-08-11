import re

def contains_only_digits(str):
    return re.match(r'^\d+$', str) is not None

def validate_problems(problems):
  if len(problems) > 5:
    raise Exception("Error: Too many problems.")

def parse_problems(problems):
  problem_length = []
  first_operands = []
  second_operands = []
  operators = []
  
  for problem in problems:
    [operand1, operator, operand2] = problem.split()
    if operator != '+' and operator != '-':
      raise Exception("Error: Operator must be '+' or '-'.")
    first_operands.append(operand1)
    second_operands.append(operand2)
    operators.append(operator)
    problem_length.append(max(len(operand1), len(operand2)))

  return [first_operands, second_operands, operators, problem_length]

def create_number_lines(input, numbers, operators, length):
    for number, operator, length in zip(numbers, operators, length):
      input += operator + " "
      fill = (length - len(number)) * " "
      spacing = 4 * " "
      input += fill + number + spacing
    return input.rstrip() + "\n"

def create_border_line(input, length_list):  
    for length in length_list:
      border = (length + 2) * "-"
      spacing = 4 * " "      
      input += border + spacing
    return input.rstrip() + "\n"

def create_result_line(input, first_operands, second_operands, operators, length_list):
      for first_operand, second_operand, operator, length in zip(first_operands, second_operands, operators, length_list):
        if operator == "+":
          result = str(int(first_operand) + int(second_operand))
        else:
          result = str(int(first_operand) - int(second_operand))

        fill = (length + 2 - len(result)) * " "
        spacing = 4 * " "
        input += fill + result + spacing
      return input.rstrip() + "\n"

def arithmetic_arranger(problems, show_result = False):
  try:
    validate_problems(problems)
    first_operands, second_operands, operators, problem_length = parse_problems(problems)
  
    if any(l > 4 for l in problem_length):
      return "Error: Numbers cannot be more than four digits."
    if not all(contains_only_digits(str) for str in first_operands + second_operands):
      return "Error: Numbers must only contain digits."

    empty_operators = [" " for _ in range(len(operators))]
    return_str = create_number_lines("", first_operands, empty_operators, problem_length)
    
    return_str = create_number_lines(return_str, second_operands, operators, problem_length)

    return_str = create_border_line(return_str, problem_length)
  
    if show_result:
      return_str = create_result_line(return_str, first_operands, second_operands, operators, problem_length)

    return return_str.rstrip()
  
  except Exception as e:
    return e.args[0]
  