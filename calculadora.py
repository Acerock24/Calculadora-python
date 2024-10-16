def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def calculadora():
    print("Bienvenido a la calculadora simple")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Ingresa el número de la operación: ")
    
    if opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    calculadora()
    