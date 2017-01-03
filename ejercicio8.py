lista1 = ["pedro","pablo","javier","omar"]
lista2 = ["gato","perr","caballo","pedro"]
def superposicion(lista1,lista2):
 
    for i in lista1:       
        for j in lista2:
            if i == j:
               print True
            else:
               print False
superposicion(lista1,lista2) 
