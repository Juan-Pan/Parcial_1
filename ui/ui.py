from tabulate import tabulate  # Librería para imprimir tablas bonitas

def mostrar_datos(datos):
    """Muestra los datos en formato de tabla."""
    if not datos:
        print("No se encontraron datos para la consulta.")
        return
    
    tabla = []
    for item in datos:
        fila = [
            item.get("ciudad_municipio_nom", "N/A"),
            item.get("departamento_nom", "N/A"),
            item.get("edad", "N/A"),
            item.get("fuente_tipo_contagio", "N/A"),
            item.get("estado", "N/A"),
        ]
        tabla.append(fila)

    encabezados = ["Ciudad", "Departamento", "Edad", "Tipo de Contagio", "Estado"]
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))
