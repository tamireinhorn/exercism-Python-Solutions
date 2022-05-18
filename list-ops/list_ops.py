from copy import copy


def append(list1, list2):
    return list1 + list2


def concat(lists):
    if not lists:
        return lists
    end = lists[0]
    for list in lists[1:]:
        end = append(end, list)
    return end
    

def filter(function, list):
    new_list = []
    for element in list:
        if function(element):
            new_list = append(new_list, [element])
    return new_list


def length(list):
    size = 0
    for element in list:
        size += 1
    return size


def map(function, list):
    new_list = []
    for element in list:
        new_list = append(new_list, [function(element)])
    return new_list


def fold_with(function, list, prior):
    if not list:
        return prior
    for element in list:
        prior = function(prior, element)
    return prior

def foldl(function, list, initial):
    
    def aux_func(prior, element):
        return function(prior, element)
        
    return fold_with(aux_func, list, initial)


def foldr(function, list, initial):
    
    def aux_func(prior, element):
        return function(element, prior)
        
    return fold_with(aux_func, reverse(list), initial)
    
def reverse(list):
    list_size = length(list)
    reverse_list = [None] * list_size
    for element, index in zip(list, range(list_size)):
        reverse_list[list_size - index -1] = element
    return reverse_list
