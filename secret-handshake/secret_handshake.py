COM = ['wink', 'double blink', 'close your eyes', 'jump']
def commands(binary_str):
    handshake = []
    for couple in zip(binary_str[::-1],COM):
        if couple[0] == '1':
            handshake.append(couple[1])
    if binary_str[0] == '1':
        handshake = handshake[::-1]

    return handshake
            
        
        
