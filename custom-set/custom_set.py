from copy import copy


class CustomSet:
    def __init__(self, elements=[]):
        self.__dict = {}
        for element in elements:
            self.add(element)
 
    def isempty(self):
        return len(self.__dict) == 0

    def __contains__(self, element):
        return element in self.__dict

    def issubset(self, other):
        for element in self.__dict:
            if element not in other:
                return False 
        return True 

    def isdisjoint(self, other):
        for element in self.__dict:
            if element in other:
                return False 
        return True 

    def __eq__(self, other):
        return self.__dict == other.__dict

    def add(self, element):
        self.__dict[element] = element

    def intersection(self, other):
        intersect_set = CustomSet()
        for element in self.__dict:
            if element in other:
                intersect_set.add(element)
        for element in other.__dict:
            if element in self:
                intersect_set.add(element)
        return intersect_set

    def __sub__(self, other):
        difference_set = CustomSet()
        for element in self.__dict:
            if element not in other:
                difference_set.add(element)
        return difference_set

    def __add__(self, other):
        union_set = copy(self)
        for element in other.__dict:
            if element not in union_set:
                union_set.add(element)
        return union_set
