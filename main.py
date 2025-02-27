from api.api import obtener_datos
from ui.ui import mostrar_datos

def main():
    departamento = input("Ingrese el nombre del departamento a consultar: ").strip().upper()
    limite = int(input("Ingrese el número de registros a obtener: ").strip())

    datos = obtener_datos(departamento, limite)
    mostrar_datos(datos)

if __name__ == "__main__":
    main()

