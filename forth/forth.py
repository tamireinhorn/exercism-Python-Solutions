class StackUnderflowError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

SUPPORTED_OPERANDS = ['+', '-', '/', '*']


def operate(operator: str, stack: list[str]):
    try:
        return eval(f'{stack[0]} {operator} {stack[1]}')
    except ZeroDivisionError:
        raise ZeroDivisionError("divide by zero")


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
    return list(map(int, stack))
