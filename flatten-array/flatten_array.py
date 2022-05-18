def flatten(object):
    master_list = []
    for element in object:
        if isinstance(element, list):
            x = flatten(element)
            master_list += x
        elif element != None:
           master_list.append(element)
    return master_list