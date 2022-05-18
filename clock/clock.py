
class Clock:
    def __init__(self, hour, minute):
        if minute < 0:
            print(hour,  abs(minute) // 60 )
            hour -= 1 + abs(minute) // 60 
            minute = 60 - abs(minute) % 60 
        if minute >= 60:
            hour += minute // 60 
            minute = minute % 60  
        if hour < 0:
            hour = 24 - abs(hour) % 24
        if hour >= 24:
            hour =  hour % 24   
        self.hour = hour
        self.minute = minute

    
    def __repr__(self):
        hour = self.hour
        minute = self.minute
        hour_string = str(hour)
        minute_string = str(minute)
        if minute < 10:
            minute_string = '0' + str(minute)
        if hour < 10:
            hour_string = '0' + str(hour) 
        return f"{hour_string}:{minute_string}"

    
    def __eq__(self, other):
        return (other.hour == self.hour) and (other.minute == self.minute)

    
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)


    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
