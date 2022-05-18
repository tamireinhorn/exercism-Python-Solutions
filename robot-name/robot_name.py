import string, random
ALPHABET = string.ascii_uppercase
robot_names = set()
class Robot:
    def __init__(self):
        self.name = self.generate_name()
        
    
    def generate_name(self):
        letters = ''.join(random.sample(ALPHABET,  2))
        numbers = ''.join(list(map(str,(random.sample(range(10), 3)))))
        name = f'{letters}{numbers}'
        while name in robot_names:
            letters = ''.join(random.sample(ALPHABET,  2))
            numbers = ''.join(list(map(str,(random.sample(range(10), 3)))))
            name = f'{letters}{numbers}'
        robot_names.add(name)
        return name 

    def reset(self):
        self.name = self.generate_name()