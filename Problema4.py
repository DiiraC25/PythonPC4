import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate"]
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def guardar_precio_bitcoin(precio):
    try:
        with open("bitcoin_prices.txt", "a") as f:
            f.write(precio + "\n")
        print("Precio de Bitcoin almacenado exitosamente en bitcoin_prices.txt")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def main():
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin:
        guardar_precio_bitcoin(precio_bitcoin)

if __name__ == "__main__":
    main()