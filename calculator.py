#!/usr/bin/env python

import collections
from operator import add, sub, mul, truediv

# Define operators by their equivalent input strings
operators = {'+': add, '-': sub, '*': mul, '/': truediv}
# Save all test cases for quick checking
test_cases = [
    # Prefix calculator
    '3', '+ 1 2', '+ 1 * 2 3', '+ * 1 2 3', '- / 10 + 1 1 * 1 2', '- 0 3', '/ 3 2'
    # Infix calculator
    , '( 1 + 2 )', '( 1 + ( 2 * 3 ) )', '( ( 1 * 2 ) + 3 )', '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )'
]


def prefix_calcuator(input: str):
    # Take an input string and calculate prefix calculator result
    # Track numbers via deque
    numbers = collections.deque()
    # Remove spaces and traverse through string right to left
    for value in input.split(' ')[::-1]:
        if value.isnumeric():
            # Add latest number to front of the queue
            numbers.appendleft(float(value))
        else:
            # Get the most recent two numbers and perform the found operator on them
            n1 = numbers.popleft()
            n2 = numbers.popleft()
            if value in ['/', '*', '+', '-']:
                # Add the result to the front of the number queue
                numbers.appendleft(operators[value](n1, n2))
            else:
                return ValueError('Invalid operator, operands or expression entered')
    # For accidental cases such as '+ 4 5 5' which would otherwise return 9
    if len(numbers) > 1:
        return ValueError('Not enough operators were given')
    return numbers[0]


def infix_calcuator(input: str):
    # Remove spaces to extract numbers, operators and parenthesis in a list
    filter_input = input.split(' ')
    # These queues will track which operators and numbers we have traversed for later computation
    numbers = collections.deque()
    operators_track = collections.deque()
    for value in filter_input:
        if value == '(':
            # Ignore forward parenthesis as they do not tell us anything of interest
            continue
        elif value == ')':
            # If a close bracket is found then calculate the value from the most recent operator and two numbers
            # Add the result to the front of the numbers as we are traversing left to right
            n2 = numbers.pop()
            n1 = numbers.pop()
            numbers.append(operators_track.pop()(n1, n2))
        elif value in ['/', '*', '+', '-']:
            # Add operator to the front of the operator queue when found
            operators_track.append(operators[value])
        elif value.isnumeric():
            # Add number to the front of the number queue when found
            numbers.append(float(value))
        else:
            return ValueError('Invalid operator, operand or expression entered')

    # For cases where more parenthesis need to be added like ( 1 / ( 1 - 10 ) - ( 1 * 2 ) )
    if len(numbers) > 1 and len(operators) > 1:
        return ValueError('Not assuming BODMAS please use enough parenthesis')
    # For cases where parenthesis are wrong like ( ( ( 1 / ( 1 - 10 ) - ( 1 * 2 ) )
    if len(numbers) > 1:
        return ValueError('Not enough operators or parenthesis were given')
    return numbers[0]


def get_result(input: str):
    # Simple way of determing which calc to use
    if '(' in input:
        output = infix_calcuator(input)
        calc = 'infix'
    else:
        output = prefix_calcuator(input)
        calc = 'prefix'
    return {'result': output, 'calc': calc}


if __name__ == "__main__":
    print("Running for test cases...")
    for test_case in test_cases:
        output = get_result(test_case)
        print(f'Input: {test_case}, Output: {output["calc"]}, Result: {output["result"]}')
    print()
    print('Note: ')
    print('     Prefix expressions must have outer parenthesis i.e. ( 1 + 1 ).')
    print('     Single spaces must be between all numbers, operators and parenthesis for both calculators.')
    print()
    while True:
        new_case = input("Enter new expression:  ")
        if new_case == "":
            break
        output = get_result(new_case)
        print(f'Input: {new_case}, Calculator: {output["calc"]}, Output: {output["result"]}')
        print()

