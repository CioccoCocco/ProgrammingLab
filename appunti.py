print("INIZIO DEGLI APPUNTI")

var1 = 5
var2 = 7
print('valore 1: {} Valore 2: {}'.format(var1, var2))
print('valore A: {A} Valore B: {B}'.format(A=1, B=2))

intero = 7
floating = 1.1
stringhe = 'stringa'
stringhe2 = "stringa"
booleano = True
nullo = None

stringhe[2]     #* secondo carattere della stringa
stringhe[-1]    #* penultimo carattere della stringa
stringhe[3:7]   #* stringa dal 3 al 7 carattere
stringhe[3:-1]  #* stringa dal 3 al penultimo carattere
stringhe[3:-1:2]  #* stringa dal 3 al penultimo carattere con un intervallo di 2 caratteri

stringaConcat = stringhe + stringhe2
stirngheMoltiplicate = stringhe*3

#! le stringhe sono IMMUTABILI: una volta create, i loro caratteri non cambiano
#? puoi soltanto creare una nuova stinga o sovrascrivere quella vecchia

esponenziale = intero ** intero     #* n^m
divisioneIntera = intero // intero  #* ritorna solo la parte intera

if (intero > floating):
    print("Ce l'ho più grosso ahahah")
    
    if(intero - floating < 1):
        print("Mica tanto")
elif (floating>intero):
    print("Ce l'ho piccolo...")
else:
    print("LETSGOSKI")

for character in stringhe:
    print(character)

i = 0
while i < 10:
    print(i)
    i+=1

for i in range(10):
    print(i)

for i,character in enumerate(stringhe):
    print("Cartattere {} in posizione {}".format(i,character))

def funzione(argomento1, argomento2):
    print("Argomento1 {}, Argomento2 {}".format(argomento1,argomento2))

funzione(intero, floating)

def funzioneRitornante(numero):
    return numero*numero

print(funzioneRitornante(intero))

def funzioneConDefault(numero, n=2):
    return numero**n #* SE NON PASSO n, n=2, ma posso passargli quello che voglio io

print(funzioneConDefault(7))
print(funzioneConDefault(7, 3))

def funzioneDocString(numero):
    """
    un commento con più righe che appare se qualcuno
    scrive qualcosa tipo:
    help(funzioneDocString)
    
    scrivici qua le cose importanti così che la gente
    capisca cosa fa la tua funzione
    """
    return numero

#! scope: LOCAL >> ENCLOSING >> GLOBAL >> BUILT-IN ---> (LEGB)
#* una buona funzione lavora solo su variabili locali (non in POO, ma va bene)

vettore = []

for i in range(10):
    vettore.append(i)
    
import math
print(math.sqrt(600))

### _che è uguale a..._
###
### form math import sqrt
### print(sqrt(600))

listaNumeri = [1, 2, 3]
listaStringhe = ["Andrea", "è", "Frocio"]
listaMista = [1, "enacoiD", 1.5, ["orcodio", 4]]

if ("frocio" in listaStringhe):
    print("Non si dice, birbante")

#* le liste condividono i metodi di stepping delle stringhe

listaNumeriCopiata = listaNumeri.copy()
#? listaNumeri è un puntatore, quindi se non usassi copy() otterrei due puntatori
#? allo stesso elemento, così invece sono due elementi diversi
#! listaNumeriCopiata = listaNumeri SONO LO STESSO OGGETTO

sottolistaNumeri = listaNumeri[:]   #* anche così sono liste diverse, o meglio, la prima è una sottolista

tupla1 = (2,)
tupla2 = 2,
#* sono elementi immutabili che possono avere più valori contemporaneamente
(a, b, c) = (1, 2, 3)

dizionario = {
    "chiave1" : 4,
    "chiave2" : 7
    #? stringa -> numero        IN QUESTO CASO (posso fare quello che voglio)
}

dizionario["chiave3"] = 10  #*aggiunge in automatico la coppia chiave/valore, dato che non esiste
del dizionario["chiave2"]

dizionario2 = {
    4 : "chiave1",
    7 : "chiave2"
    #? CHIAVE IMMUTABILE -> elemento
}

collezioneSet = set("abracadabra")  #* collezione non ordinata di oggetti UNICI e IMMUTABILI

#* set("abracadabra") == ("a", "b", "r", "c", "d")
#? i set supportano operazioni insiemistiche ( AND = &, OR = |, + e - )

#* https://pythontutor.com/python-compiler.html-mode=edit compilatore Python online 

#** FILE **

my_file = open("filename.txt", "r")
content = my_file.read()
print(content)
for line in my_file:
    print(line)
my_file.close()

#per non dover aprire e chiudere il file...
with open("filename.txt", "r") as my_file2:
    content = my_file.read()
    print(content)

with open("filename.txt", "w") as my_file3:
    my_file3.write("Ciao mondo!")

with open("commaseparated.txt", "r") as commafile:
    for line in commafile:
        elementi = line.split(",")  # [1, 2]
        print(elementi)

#* with può essere utilizzato con oggetti che hanno i metodi __enter__ e __exit__
#* con il metodo __enter__ si esegue il codice prima di entrare nel with
#* con il metodo __exit__ si esegue il codice dopo l'uscita dal with
#? file di rete, file compressi, connessioni database, lock... e ovviamente oggetti custom con quei metodi

#** CLASSI **

#* snake_case per metodi, variabili e istanze
#* camelCase per le classi

#* private method ==> __method__
#? dir(istanza_oggetto) stampa tutti gli attributi e i metodi della classe istanziata

class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return 'Person "{} {}"'.format(self.name, self.surname)
    
class Student(Person):
    def __init__(self, name, surname, number):
        super().__init__(name, surname)
        self.number = number
        
    def __str__(self):
        return super().__str__ + 'Student number "{}"'.format(self.number)

person = Person("Mario", "Rossi")
print(person)
print(person.name)
print(person.surname)

student = Student("Andrea", "Marino", "s326255")
print(student)
print(student.name)
print(student.surname)
print(student.number)

#---------#---------#---------#---------#---------#---------#---------#--------