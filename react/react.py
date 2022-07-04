

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
    
    @property
    def value(self):
        print('I got called here')
        return self._value
    
    @value.setter
    def value(self, new_value):
        print('Setting new value_')
        self._value = new_value

class ComputeCell:
    def __init__(self, inputs: list[InputCell], compute_function):
        self._inputs = [input.value for input in inputs]
        self.value = compute_function(self._inputs)

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
