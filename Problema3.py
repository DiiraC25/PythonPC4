import requests
import zipfile
from io import BytesIO

def descargar_imagen(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Error al descargar la imagen:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Error de solicitud:", e)
        return None

def guardar_imagen_como_zip(imagen, nombre_archivo):
    with zipfile.ZipFile(nombre_archivo, 'w') as zipf:
        zipf.writestr('imagen.jpg', imagen)

def extraer_zip(nombre_archivo):
    with zipfile.ZipFile(nombre_archivo, 'r') as zipf:
        zipf.extractall()

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    imagen = descargar_imagen(url_imagen)
    if imagen:
        guardar_imagen_como_zip(imagen, "imagen.zip")
        print("Imagen descargada y almacenada como imagen.zip")
        extraer_zip("imagen.zip")
        print("Imagen extraída de imagen.zip")
    else:
        print("No se pudo descargar la imagen.")

if __name__ == "__main__":
    main()