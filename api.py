from sodapy import Socrata

def obtener_datos(departamento, limite):
    """Consulta los datos de COVID-19 desde la API y devuelve los resultados filtrados."""
    client = Socrata("www.datos.gov.co", None)
    resultados = client.get("gt2j-8ykr", limit=limite, departamento_nom=departamento)
    return resultados
