# s_0 = 1, s_i = 3s_(i-1) / 2

# P(x,z) = { s_i | i >= 0, i € N, x <= s_i <= z}

class Successione():
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    def __iter__(self):
        self.s = 1
        while self.s < self.x:
            self.s = 3*self.s/2
        return self
    
    def __next__(self):
        if self.s > self.z:
            raise StopIteration
        else:
            self.s = 3*self.s/2
            return 2*self.s/3
            

# x, x+d, x+2d, x+3d,..., y

class Deltoide():
    def __init__(self, x, d, y):
        self.x = x
        self.d = d
        self.y = y
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.x <= self.y:
            self.x += self.d
            return self.x - self.d
        else:
            raise StopIteration
        
for x in Deltoide(1, 0.5, 3):
    print(x)
    
class EstPrime():
    def __init__(self, elements):
        self.elements = elements
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.elements)-1:
            while self.i < len(self.elements):
                number = self.elements[self.i]
                self.i+=1
                if self.isPrimo(number):
                    return number
        else:
            raise StopIteration
               
    def isPrimo(self, n):
        for k in range(2, n):
            if( n % k == 0 ):
                return False
            
        return True

lista = [10, 15, 3, 7, 12, 19, 4]
for items in EstPrime(lista):
    print(items)