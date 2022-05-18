import re

def header_parsing(line):
    header_match = re.match('#{1,6} ', line) # A header is composed of 1 to 6 #s and a space.
    if header_match:
        size = header_match.end() -1 # We remove the space's position.
        line = f'<h{size}>{line[(size+1):]}</h{size}>' # This is the pattern of the header.
    return line


def add_paragraph(line):
    # This verifies for any of the possible tags. If they aren't there, you add the paragraph marker.
    paragraph_match = re.match('<h|<ul|<p|<li', line)
    if not paragraph_match:
        line = f"<p>{line}</p>"
    return line

# These must be two functions because you CAN have both bold and italics. 
def parse_bold(line):
    bold_match = re.match('(.*)__(.*)__(.*)', line) # Look for bold
    if bold_match:
        line = f"{bold_match.group(1)}<strong>{bold_match.group(2)}</strong>{bold_match.group(3)}" # parse bold
    return line


def parse_italic(line):
    italic_match = re.match('(.*)_(.*)_(.*)', line) # Look for italics.
    if italic_match:
        line = f"{italic_match.group(1)}<em>{italic_match.group(2)}</em>{italic_match.group(3)}" # parse italics.
    return line 


def parse_bold_italics(line):
    return parse_italic(parse_bold(line))


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        i = header_parsing(i)
        list_match = re.match(r'\* (.*)', i) # Here we match for an *, which indicates a list
        if list_match: # If you have a list
            curr = list_match.group(1) # This gets whatever comes after the list signaling
            curr = parse_bold_italics(curr)
            i = f"<li>{curr}</li>" # Anything inside a list gets the list item tag.
            if not in_list:
                in_list = True # We mark that we are now inside of a list
                i = f"<ul>{i}" # The first part of the list will put an <ul> in the beggining of the list.
        else: # If we don't match for a list
            if in_list: # If we WERE inside a list
                in_list_append = True
                in_list = False # Now we are out, because we've seen its end in another line. 
        i = add_paragraph(i)
        i = parse_bold_italics(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
