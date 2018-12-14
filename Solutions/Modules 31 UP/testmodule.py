import math

def add(a,b):
    addition=a+b
    print (addition)
    return

def sub(a,b):
    subtraction=a-b
    print (subtraction)
    return

def div(a,b):
    divide=a/b
    return round(divide,2)

def mult(a,b):
    multiply=a*b
    print (multiply)
    return

def expo(a,b):
    exponential=a**b
    print (exponential)
    return

def perc(a,b):
    percent1=(a/b)*100
    percent2= str(round(percent1))+"%"
    return percent2

def mod(a,b):
    modulus=a%b
    return modulus

def divrem(a,b):
    ast=str(a)
    bst=str(b)
    floor=str(math.floor(div(a,b)))
    modst=str(mod(a,b))
    print(ast+"/"+bst+" = "+floor+", remainder: "+modst)
    return 
    


    

    
