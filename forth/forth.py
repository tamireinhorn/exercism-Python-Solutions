from copy import copy
import re 

class StackUnderflowError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

SUPPORTED_OPERANDS = ['+', '-', '/', '*']

def operate(operator: str, stack: list[str]) -> int:
    try:
        return eval(f'{stack[0]} {operator} {stack[1]}')
    except ZeroDivisionError:
        raise ZeroDivisionError("divide by zero")


def _duplicate(stack: list[str]) -> list[str]:
    return stack + [stack[-1]]


def _drop(stack: list[str]) -> list[str]:
    new_stack = copy(stack)
    new_stack.pop()
    return new_stack


def _swap(stack: list[str]) -> list[str]:
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    return stack[0:len(stack) -2] + [stack[-1], stack[-2]]

def _over(stack: list[str])-> list[str]:
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    return stack + [stack[-2]]

WORD_DICT = {'dup': _duplicate, 'drop': _drop, 'swap': _swap, 'over': _over}


def user_defined_function(input_data) -> list[str]:
    for i in input_data:
        if ':' in i:
            parsed_input_data = i.split(' ')
            definition = parsed_input_data[1]
            if definition.replace('-', '').isdigit():
                raise ValueError('illegal operation')
            replacement = ' '.join(parsed_input_data[2:len(parsed_input_data) -1])
    if definition in SUPPORTED_OPERANDS or replacement in SUPPORTED_OPERANDS:
        input_data[-1] = input_data[-1].replace(definition, replacement)
    else:
        input_data[-1] = re.sub(definition, replacement, input_data[-1], flags= re.IGNORECASE)
    return input_data


def evaluate(input_data):
    if ':' in input_data[0]:
        input_data = user_defined_function(input_data)
    parsed_input_data = input_data[-1].split(' ')
    stack = []
    for item in parsed_input_data:
        if item.replace('-', '').isdigit():
            stack.append(item)
        elif item in SUPPORTED_OPERANDS:
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack = [operate(item, stack)]
        elif item.lower() in WORD_DICT:
            if len(stack) == 0:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack = WORD_DICT[item.lower()](stack)
        else:
            raise ValueError('undefined operation')
    return list(map(int, stack))

