import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = float(data["bpi"]["USD"]["rate_float"])
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    precio_usd = obtener_precio_bitcoin()

    if precio_usd is not None:
        costo_usd = cantidad_bitcoins * precio_usd
        print(f"El costo actual de {cantidad_bitcoins} bitcoins en USD es: ${costo_usd:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()