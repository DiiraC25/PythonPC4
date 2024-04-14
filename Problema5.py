def guardar_tabla_multiplicar(numero):
    if 1 <= numero <= 10:
        with open(f"tabla-{numero}.txt", "w") as f:
            for i in range(1, 11):
                f.write(f"{numero} x {i} = {numero * i}\n")
        print(f"La tabla de multiplicar del {numero} ha sido guardada en tabla-{numero}.txt")
    else:
        print("El número debe estar entre 1 y 10.")


def mostrar_tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")


def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as f:
            lineas = f.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1])
            else:
                print("El número de línea está fuera del rango.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea ver: "))
            mostrar_linea_tabla(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()