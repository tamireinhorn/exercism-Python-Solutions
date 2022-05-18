def roman(number: int) -> str:
    one = "I"
    five = "V"
    ten = "X"
    fifty = "L"
    hundred = "C"
    fivehundred = "D"
    thousand = "M"
    romans = [(one, five, ten), (ten, fifty, hundred), (hundred, fivehundred, thousand), thousand]
    answer = []
    for couple in zip(str(number)[::-1], romans):
        digit = int(couple[0])
        print(couple)
        if digit == 0:
            continue
        if 1 <= digit <=3:
            answer.append(digit * couple[1][0])
        elif  digit<= 5:
            answer.append(couple[1][0] * (5 - digit) + couple[1][1])
        elif digit <= 8:
            answer.append( couple[1][1] + (digit - 5) * couple[1][0])
        elif digit == 9:
            answer.append( couple[1][0] + couple[1][2])

    return ''.join(answer[::-1])