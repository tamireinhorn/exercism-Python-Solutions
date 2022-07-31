
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
        if new_value != self.value:
            self._value = new_value
            for dependent_cell in self._dependent_cells: # First, update every dependent cell from the input
                dependent_cell._update()
            for dependent_cell in self._dependent_cells: # Then have the dependent cells propagate.
                dependent_cell._propagate()
        

class ComputeCell:
    def __init__(self, inputs: list[any], compute_function):
        self._dependent_cells = []
        for cell in inputs:
            cell._dependent_cells.append(self) # So you add to the cells, the current compute cell that depends on it!
        self._inputs = inputs
        self._callbacks = {}
        self._calculate_value = lambda: compute_function([v.value for v in self._inputs])
        self._value = self._calculate_value()
        # Now, we need to add to every one in 

    @property
    def value(self):
        return self._value # The value is updated when called!
    
    def _update(self):
        new_value = self._calculate_value()
        if self._value != new_value: # Only updating on change
            self._value = new_value # Update the value
           
    
    def _propagate(self):
        current_value = self._value
        for dependent_cell in self._dependent_cells: # Propagate the change.
            dependent_cell._update()
            dependent_cell._propagate()
        for callback in self._callbacks: 
            callback(self._value)

    def add_callback(self, callback):
        self._callbacks[callback] = callback
        return callback

    def remove_callback(self, callback):
        self._callbacks.pop(callback, '')
