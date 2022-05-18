def convert(number: int) -> str:
    answer = ""
    has_3_factor = number % 3 == 0
    has_5_factor = number % 5 == 0
    has_7_factor = number % 7 == 0
    if has_3_factor:
        answer += "Pling"
    if has_5_factor:
        answer += "Plang"
    if has_7_factor:
        answer += "Plong"
    
    return answer or str(number) #Falsiness of answer:
    #If answer is an empty string, it's interpreted as False!
