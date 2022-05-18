def response(hey_bob):
    hey_bob = hey_bob.replace(' ', '').replace('\t', '').replace('\r', '').replace('\n', '')
    try:
        is_question = hey_bob[-1] == '?'
    except:
        is_question = False
    has_letters =  any(c.isalpha() for c in hey_bob)
    is_yell = hey_bob.upper() == hey_bob and has_letters
    if is_yell:
        if is_question:
            answer = "Calm down, I know what I'm doing!"
        else:
            answer = "Whoa, chill out!"
    elif is_question:
        answer = "Sure."
    elif len(hey_bob) == 0:
        answer = "Fine. Be that way!"
    else:
        answer = "Whatever."
    return answer
