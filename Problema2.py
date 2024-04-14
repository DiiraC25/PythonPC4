from pyfiglet import Figlet
import random

def seleccionar_fuente():
    figlet = Figlet()
    fuentes = figlet.getFonts()
    fuente_seleccionada = input(f"Selecciona una fuente ({', '.join(fuentes)}): ").strip()
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes)
    return fuente_seleccionada

def main():
    fuente = seleccionar_fuente()
    texto = input("Ingrese el texto: ")
    figlet = Figlet(font=fuente)
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()