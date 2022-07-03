

class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value


class ComputeCell:
    def __init__(self, inputs: list[InputCell], compute_function):
        self._inputs = [input.value for input in inputs]
        self.value = compute_function(self._inputs)

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
