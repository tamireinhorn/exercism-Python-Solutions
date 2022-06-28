from copy import copy


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


WORD_DICT = {'dup': _duplicate, 'drop': _drop, 'swap': _swap}


def evaluate(input_data):
    parsed_input_data = input_data[0].split(' ')
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
    return list(map(int, stack))
