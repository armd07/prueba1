"""suma y multiplicacion"""
lista1 = range(0,20,1)
print lista1
def sum(lista1):
    s = 0
    for i in lista1:
       s += i    
    print "La suma de los valores de la lista: ",s

sum(lista1)

lista2 = range(1,4,1)
print lista2
def mul(lista2):
    m = 1
    for j in lista2:
        m *= j
    print "La multiplicacion de los valores de lista es: ",m
mul(lista2)
