from copy import copy
from operator import methodcaller

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
    replacement_dict = {}
    replacement = ''
    for i in input_data:
        if ':' in i:
            parsed_input_data = i.split(' ')
            definition = parsed_input_data[1]
            if definition.replace('-', '').isdigit():
                raise ValueError('illegal operation')
            for index, _ in enumerate(parsed_input_data[2:len(parsed_input_data) -1]):
                parsed_input_data[2+index] = parsed_input_data[2+index].replace(definition, replacement)
            replacement = ' '.join(parsed_input_data[2:len(parsed_input_data) -1])
            if replacement in replacement_dict:
                replacement = replacement_dict[replacement]
            replacement_dict.update({definition: replacement})
    for definition, replacement in replacement_dict.items():
        input_data[-1] = input_data[-1].replace(definition, replacement)
    return input_data


def evaluate(input_list):
    input_data = list(map(methodcaller('lower'), input_list))
    if ':' in input_data[0]:
        input_data = user_defined_function(input_data)
    parsed_input_data = input_data[-1].split(' ')
    stack = []
    for item in parsed_input_data:
        item = item.lower()
        if item.replace('-', '').isdigit():
            stack.append(item)
        elif item in SUPPORTED_OPERANDS:
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack = [operate(item, stack)]
        elif item in WORD_DICT:
            if len(stack) == 0:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack = WORD_DICT[item](stack)
        else:
            raise ValueError('undefined operation')
    return list(map(int, stack))

