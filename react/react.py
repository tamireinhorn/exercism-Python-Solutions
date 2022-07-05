CELL_LIST = []
class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        CELL_LIST.append(self)
    
    @property # This is the recommended way to use a property decorator, right above where the attribute will be returned.
    def value(self):
        return self._value
    
    # In reality, property is an object with three methods, getter, setter and deleter.
    # So when we specify value as a property, we can then create a value setter method with the same name, just by using the decorator above.
    @value.setter
    def value(self, new_value):
        #TODO: If the new value is different than the old one, we should make the Compute cell value be done again. But how?
        # The big issue here is that the Compute Cell is OUTSIDE of this scope. How do I call anything on it?
        self._value = new_value

class ComputeCell:
    def __init__(self, inputs: list[InputCell], compute_function):
        self._inputs = [input.value for input in inputs]
        self._function = compute_function
        self._callbacks = {}

    @property
    def value(self):
        return self._function(self._inputs)
    
    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        try:
            del self._callbacks[callback]
        except:
            raise KeyError
