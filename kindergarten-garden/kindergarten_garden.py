from itertools import chain
STUDENTS = ["Alice", "Bob", "Charlie", "David",
"Eve", "Fred", "Ginny", "Harriet",
"Ileana", "Joseph", "Kincaid","Larry"]
NUMBER_OF_CUPS = 2
PLANTS = {'R': 'Radishes', 'V': 'Violets', 'G': 'Grass', 'C': 'Clover'}


class Garden:
    def __init__(self, diagram: str, students: list[str] = STUDENTS):
        self.diagram = diagram
        self.students = students


    def plants(self, student:str) -> list[str]:
        diagram = self.diagram
        students = self.students
        students.sort()
        rows = diagram.split('\n')
        try:
            student_position = students.index(student)
        except:
            raise ValueError('This student is not in the class.')
        return list(chain.from_iterable([[PLANTS.get(plant) for plant in row[(student_position * NUMBER_OF_CUPS):((student_position * NUMBER_OF_CUPS)+NUMBER_OF_CUPS)]] for row in rows]))