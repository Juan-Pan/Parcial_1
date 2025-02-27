from sodapy import Socrata

def obtener_datos(departamento, limite):
    """Obtiene los datos de COVID-19 desde la API de Datos Abiertos."""
    client = Socrata("www.datos.gov.co", None)  # Sin autenticación
    resultados = client.get("gt2j-8ykr", limit=limite, where=f"departamento_nom = '{departamento}'")

    return resultados
