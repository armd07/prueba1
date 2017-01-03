""" funcion palindromo"""

a = raw_input("ingrese palabra: ")
def palindromo(a):
    b = a[::-1]
    if b == a:
        print True
    else:
        print False    
        print b

palindromo(a)
     
