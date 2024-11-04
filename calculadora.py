# CALCULADORA SIMPLE DE PYTHON

print("CALCULADORA")



def calculadora(num1, num2, operacion):
    if operacion == 1:  
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        return num1 / num2  
    else:
        return "Operacion no valida"

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operacion = int(input("Ingrese la operacion a realizar ( 1: suma, 2: resta, 3: multiplicacion, 4: division,): "))

print("El resultado es: ",(calculadora(num1, num2, operacion)))