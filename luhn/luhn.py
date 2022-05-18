
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        clean_num = self.card_num.strip().replace(' ', '')
        if len(clean_num) == 1:
            return False
        
        try:
            int(clean_num)
        except:
            return False 
        clean_num_list = list(clean_num)
        y = lambda x: x - 9 if x > 9 else x 
        luhn_list = [y(int(element) * 2) if index % 2 != 0 else y(int(element)) for index, element in enumerate(clean_num_list[::-1])]
        

        
        
            
            
            
            
        
        return sum(luhn_list) % 10 == 0
        
            
