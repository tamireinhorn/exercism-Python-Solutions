MERCURY, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE = 0.2408467, 0.61519726, 31557600, 1.8808158, 11.862615, 29.47498, 84.016846, 164.79132

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds


    def on_earth(self):
        return round(self.seconds / EARTH, 2)


    def on_mercury(self):
        return round((self.seconds / EARTH) / MERCURY, 2)

    
    def on_venus(self):
        return round((self.seconds / EARTH) / VENUS, 2)
    

    def on_mars(self):
        return round((self.seconds / EARTH) / MARS, 2)


    def on_jupiter(self):
        return round((self.seconds / EARTH) / JUPITER, 2)
    

    def on_saturn(self):
        return round((self.seconds / EARTH) / SATURN, 2)
    

    def on_uranus(self):
        return round((self.seconds / EARTH) / URANUS, 2)


    def on_neptune(self):
        return round((self.seconds / EARTH) / NEPTUNE, 2)
    
