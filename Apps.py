
"""
    Esta funcion realiza el factorial de  un numero  
    retorna  el  factorial 
"""
from math import factorial


def fact(x):
    factorial =1
    for i in range(1,x+1):
        factorial *=i;
    return factorial


