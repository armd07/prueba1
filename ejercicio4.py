"""saber si es vocal o no"""

caracter = raw_input("Ingrese el caracter: ")
def vocal(caracter):
    if caracter == "a" or caracter =="e" or caracter == "i" or caracter == "o" or caracter == "u":
         print "El caracter ingresado es una vocal"
    elif caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
         print "El caracter ingresado es una Vocal"
    else:
         print "El caracter ingresado no es una vocal"
    return caracter

vocal(caracter)
