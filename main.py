import api  # Importa el módulo completo
from ui import mostrar_resultados  # Importa la función para mostrar los datos

def main():
    departamento = input("Ingrese el nombre del departamento a consultar: ").strip().upper()
    limite = int(input("Ingrese el número de registros a consultar: "))

    # Llamar a la función de api.py
    datos = api.obtener_datos(departamento, limite)

    # Mostrar los datos en formato de tabla
    mostrar_resultados(datos)

if __name__ == "__main__":
    main()

