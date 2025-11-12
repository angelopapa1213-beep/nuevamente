
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede divsumaridir entre cero"

print("=== Calculadora Básica ===")
print("Sumar")
print("Restar")
print("Multiplicar")
print("Dividir")

opcion = input("Elige una opción (sumar restar multiplicar dividir): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == 'sumar':
    print("Resultado:", sumar(num1, num2))
elif opcion == 'restar':
    print("Resultado:", restar(num1, num2))
elif opcion == 'multiplicar':
    print("Resultado:", multiplicar(num1, num2))
elif opcion == 'dividir':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opción no válida.")