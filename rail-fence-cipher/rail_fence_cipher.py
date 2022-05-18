import itertools
from math import modf

def encode(message: str, rails: int):
    rail_list = [list() for i in range(rails)] #Create one list for each rail
    indices  = [*[i for i in range(rails)], *[i for i in range(rails-2,0,-1)]] #The order of the lists needs to do this smart loop
    #If it's 3 rails, it should be 0, 1, 2, 1 then loop. 
    for letter,index in zip(message,itertools.cycle(indices)):
        rail_list[index].append(letter)
    return  ''.join(list(itertools.chain.from_iterable(rail_list)))
       

def decode(encoded_message, rails):
    rail_matrix = [list() for i in range(rails)]
    indices = [*[i for i in range(rails)], *[i for i in range(rails-2,0,-1)]]
    #The logic is that if walk along the rails and count the chars per rail, we know how many letters each rail will have
    #We can break the diagonals into multiple patterns, starting from the first row and ending one row before it.
    #Since these patterns are like 1 letter in the first and last row and 2 letters for the rest, they have: 2 + (n-2)*2 letters each.
    pattern_size = 2 + 2 * (rails -2)
    message_size = len(encoded_message)
    rest, number_of_patterns = modf(message_size / pattern_size)
    # So doing message size/pattern size, we might have, for example, 9/6
    # So we have 1 full pattern + 0.5 of one. That would mean 3 letters, which we would add to each of the indices until they end.
    ## This is more efficient than assembling the entire matrix by hand.
    rest = int(rest * pattern_size)
    number_of_patterns = int(number_of_patterns)
    # The rail matrix will be: number_of_patterns, (n-2) lines of 2 * number_of_patterns, number_of_patterns
    size_list = [number_of_patterns, *(rails-2) * [2 * number_of_patterns], number_of_patterns]
    #This adds the rest of the incomplete pattern to the sizes of each rail.
    for a, index in zip(range(rest), itertools.cycle(indices)):
        size_list[index]+= 1
    len_counter = 0
    #Now, we're splitting the encoded message on each rail
    for rail_num, size in enumerate(size_list):
        rail_matrix[rail_num] = list(encoded_message[len_counter:(len_counter+size)])
        len_counter+= size
    #This is what effectively reads the rails in zig zag fashion and decodes the message. 
    answer = ''
    for letter, index in zip(encoded_message, itertools.cycle(indices)):
        answer+= rail_matrix[index].pop(0)
    return answer