print("538 minuti sono: {}h:{}m".format(538//60, 538%60))

def countLetter ( string, chtr ):
    cnt = 0
    for character in string:
        if chtr == character:
            cnt+=1
    
    return cnt

print("Ci sono {} {} in {}".format(countLetter("zuzzurellone", "z"), "z", "zuzzurellone"))

def palindrome ( string ):
    bkwrds = -1
    for i in range(0, len(string)//2):
        if string[i] != string[bkwrds]:
            return False
        bkwrds-=1
    
    return True

print(palindrome("anna"))
print(palindrome("pollo"))

def triangle( a, b, c ): 
    if( (a+b >= c) & (a+c >= b) & (b+c >=a) ):
        #it can be a triangle
        if( a == b & b == c ):
            return "equilateral"
        elif( a != b & b != c & c != a ):
            return "scaleno" #non so come si dica in inglese e sono senza internet
        elif( (a == b & a != c) | (a == c & a != b) | (b == c & b != a) ):
            return "isoscele" #come sopra
    
    return "Not a triangle"

print(triangle(3, 4, 5))
print(triangle(3, 4, 12))
print(triangle(2, 2, 2))

def swap( list, i, j ):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
def factorial( n ):
    fac = 1
    for i in range(2,n):
        fac = fac * i
    return fac

def commonElement( list1, list2 ):
    for element in list1:
        if list2.contains(element):
            return True
        
    return False

def numToAlfa( list ):
    alfaList = []
    for number in list:
        if( number == 1 ):
            alfaList.append("uno")
        elif( number == 2 ):
            alfaList.append("due")
        elif( number == 3 ):
            alfaList.append("tre")
        elif( number == 4 ):
            alfaList.append("QUATTRO!")
        elif( number == 5 ):
            alfaList.append("cinque")
        elif( number == 6 ):
            alfaList.append("sei")
        elif( number == 7 ):
            alfaList.append("sette")
        elif( number == 8 ):
            alfaList.append("otto")
        elif( number == 9 ):
            alfaList.append("nove")
    
    return alfaList