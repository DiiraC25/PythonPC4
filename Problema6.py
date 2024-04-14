def contar_lineas_codigo(archivo):
    try:
        if not archivo.endswith('.py'):
            print("El archivo no tiene extensión .py.")
            return

        with open(archivo, 'r') as f:
            lineas = f.readlines()

            # Filtrar líneas en blanco y comentarios
            lineas_filtradas = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith('#')]

            print(f"Archivo: {archivo}, número de líneas de código: {len(lineas_filtradas)}")

    except FileNotFoundError:
        print("No se encontró el archivo.")


if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)