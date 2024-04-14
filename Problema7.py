import requests
import sqlite3

def obtener_datos_sunat(year):
    try:
        datos = []
        for month in range(1, 13):
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year={year}"
            response = requests.get(url)
            if response.status_code == 200:
                datos.extend(response.json())
        return datos
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API de SUNAT: {e}")
        return None

def crear_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT PRIMARY KEY,
                compra REAL,
                venta REAL
            )
        """)
        conn.commit()
        print("Tabla creada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def insertar_datos(conn, datos):
    try:
        cursor = conn.cursor()
        for dato in datos:
            cursor.execute("""
                INSERT INTO sunat_info (fecha, compra, venta)
                VALUES (?, ?, ?)
            """, (dato["fecha"], dato["compra"], dato["venta"]))
        conn.commit()
        print("Datos insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en la tabla: {e}")

def main():
    year = 2023
    datos = obtener_datos_sunat(year)
    if datos:
        conn = sqlite3.connect("base.db")
        crear_tabla(conn)
        insertar_datos(conn, datos)
        conn.close()

if __name__ == "__main__":
    main()