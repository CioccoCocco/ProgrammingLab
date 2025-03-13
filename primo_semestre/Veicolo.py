class Veicolo():
    def __init__(self, model, year, brand):
        self.model = model
        self.year = year
        self.brand = brand
        self.speed = 0
        
    def __str__(self):
        return "This vehicle is a {} {} from {}, speed is {} km/h".format(self.brand, self.model, self.year, self.speed)
    
    def accelerate(self):
        self.speed += 5
        
    def decelerate(self):
        self.speed -= 5
        
    def get_speed(self):
        return self.speed
        
class Auto(Veicolo):
    def __init__(self, model, year, brand, doors):
        super.__init__(model, year, brand)
        self.doors = doors
        
    def __str__(self):
        return super().__str__() + " with {} doors".format(self.doors)
        
class Moto(Veicolo):
    def __init__(self, model, year, brand, type):
        super.__init__(model, year, brand)
        self.type = type
    
    def __str__(self):
        return super().__str__() + " of type {}".format(self.type)
