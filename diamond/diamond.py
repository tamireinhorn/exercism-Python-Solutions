from string import ascii_uppercase 
ALPHABET = list(ascii_uppercase)
def rows(letter):
    letter_index = ALPHABET.index(letter)
    number_of_spaces = letter_index
    spaces_in_the_middle = 1
    answer = [None for i in range(2 * letter_index + 1)]
    answer = [f"{number_of_spaces * ' '}A{number_of_spaces * ' '}"] # Top and bottom is always A
    if letter == 'A':
        return answer
    for diamond_letter, number in zip(ALPHABET[1:letter_index], range(letter_index)):
        number_of_spaces -= 1
        line = f"{number_of_spaces * ' '}{diamond_letter}"
        line = f"{line}{spaces_in_the_middle * ' '}{line[::-1]}"
        answer.append(line)
        spaces_in_the_middle += 2
    reversed_answer = answer[::-1]
    middle_line = f"{letter}{spaces_in_the_middle * ' '}{letter}"
    answer.append(middle_line)
    answer += reversed_answer
    return answer
