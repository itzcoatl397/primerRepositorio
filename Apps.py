
"""
    Esta funcion realiza el factorial de  un numero  
    retorna  el  factorial 

"""
def fact(x):
    fact =1
    for i in range(1,x+1):
        fact *=i;
    return fact


