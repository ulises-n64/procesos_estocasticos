#from (nombre archivo) import (nombre funcion)

def input_int(message=""):
    return int(input(message))


def main():
    print("Por:")
    print("Rangel Huerta Alejandra")
    print("Hernandez Martinez Abraham")
    print("Ramiréz Calnacasco Ulises")
    print("Soto Aguilar Ethel")

    print()

    print("Hola usuario.")
    print("¿Qué metodo quieres resolver hoy?")
    print("1. Enumeracion exhaustiva de politicas")
    print("2. Solucion por programacion lineal")
    print("3. Metodos de mejoramiento de politicas")
    print("4. Mejoramiento de politica con descuento")
    print("5. Metodo de aproximaciones sucesivas")
   
    metodo = input_int("")

    if metodo == 1:
        print("Resolveremos por Enumeracion exhaustiva de politicas")
    elif metodo == 2:
        print("Resolveremos por Solucion por programacion lineal")
    elif metodo == 3:
        print("Resolveremos por Metodos de mejoramiento de politicas")
    elif metodo == 4:
        print("Resolveremos por Mejoramiento de politica con descuento")
    elif metodo == 5:
        print("Resolveremos por Metodo de aproximaciones sucesivas")
      
    else:
        print("No es una opcion valida por favor digite un numero de 1-5")


if __name__ == "__main__":
    main()