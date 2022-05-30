
def transpose(lines: str):
    if lines:
        # If you have A1, you want it: [A, 1]. If you have [A, 1] you want it to be 'A1'
        split_lines = lines.split('\n') # 'ABC \n 123' becomes ['ABC', '123']
        length_list = [len(line) for line in split_lines]
        max_length = max(length_list)
        split_lines_v2 = [line.replace(' ', '_').ljust(max_length) for line in split_lines] # Pad when needed, ansd also replace the original spaces for '_'
        return '\n'.join([''.join(line).rstrip().replace('_', ' ') for line in zip(*split_lines_v2)]) # Remove the extra padding if needed and remove the replacement.    
    return ""

