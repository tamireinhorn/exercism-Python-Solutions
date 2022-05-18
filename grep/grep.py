import re
def grep(pattern, flags, files):
    answer = ""
    i_flag = re.IGNORECASE if 'i' in flags else 0 # If we get i, we have to ignore case and use it. If not, no flags.
    if 'x' in flags: # The x flag asks us that we do an exact match of the entire sentence.
        match_func = lambda x: re.match(pattern, x, flags = i_flag)
    else:
        match_func = lambda x: re.search(pattern, x, flags = i_flag) # Regular regex search.
    if 'v' in flags: # The v flag inverts everything and asks we find everything that DOESN`T match.
        new_match_func = lambda x: not match_func(x)
    else:
        new_match_func = match_func
    for file in files:
        nb_lines = 0
        file_name = f"{file}:" if len(files) > 1 else "" # If we get more than 1 file, we have to identify where the line came from.
        with open(file) as f:
            if 'l' in flags: # The l flag just asks us that we return the file names where the pattern can be found.
                if pattern in f.read():
                    answer += f"{file}\n"
            else:
                for line in f.readlines(): # Now iterate over every line
                    nb_lines += 1
                    if new_match_func(line):
                        n_flag = f"{nb_lines}:" if 'n' in flags else "" # If the n flag is active, we get the number of lines. 
                        answer+= f"{file_name}{n_flag}{line}" # If the match works, it`s added to the answer variable with all the necessary flags.
    return answer
 