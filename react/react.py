
class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._dependent_cells = [] # An input cell will have everyone they need to propagate to inside this.
    
    @property # This is the recommended way to use a property decorator, right above where the attribute will be returned.
    def value(self):
        return self._value
    
    # In reality, property is an object with three methods, getter, setter and deleter.
    # So when we specify value as a property, we can then create a value setter method with the same name, just by using the decorator above.
    @value.setter
    def value(self, new_value):
        #TODO: If the new value is different than the old one, we should make the Compute cell value be done again. But how?
        # The big issue here is that the Compute Cell is OUTSIDE of this scope. How do I call anything on it?
        if new_value != self.value:
            self._value = new_value
            for dependent_cell in self._dependent_cells:
                for callback in dependent_cell._callbacks:
                    callback(dependent_cell.value)
        

class ComputeCell:
    def __init__(self, inputs: list[InputCell], compute_function):
        for input_cell in inputs:
            input_cell._dependent_cells.append(self)
        self._inputs = inputs
        self._function = compute_function
        self._callbacks = {}
        self._value = self._function([v.value for v in self._inputs])
        # Now, we need to add to every one in 

    @property
    def value(self):
        new_value =  self._function([v.value for v in self._inputs])
        return new_value
    
    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        pass
