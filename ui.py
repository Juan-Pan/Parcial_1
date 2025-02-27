from tabulate import tabulate

def mostrar_resultados(datos):
    """Muestra los resultados en formato de tabla."""
    if not datos:
        print("No se encontraron resultados.")
        return

    # Seleccionar solo las columnas necesarias
    tabla = []
    for r in datos:
        tabla.append([
            r.get("ciudad_municipio_nom", "N/A").upper(),
            r.get("departamento_nom", "N/A").upper(),
            r.get("edad", "N/A"),
            r.get("fuente_tipo_contagio", "N/A"),
            r.get("estado", "N/A")
        ])

    # Definir los encabezados
    encabezados = ["Ciudad", "Departamento", "Edad", "Tipo de Contagio", "Estado"]

    # Imprimir la tabla formateada
    print("\nResultados de la consulta:\n")
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))
