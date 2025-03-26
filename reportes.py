from archivo_json import cargar_datos

ARTISTAS_JSON = "data/artistas.json"

def artistas_por_pais_y_tiempo(pais, inicio, fin):
    """Muestra artistas de un país en un período de tiempo."""
    artistas = cargar_datos(ARTISTAS_JSON)
    
    filtrados = [
        artista for artista in artistas
        if artista["Country"] == pais and inicio <= int(artista["Release year of first charted record"]) <= fin
    ]
    
    if not filtrados:
        print(f"⚠ No hay artistas de {pais} entre {inicio} y {fin}.")
        return

    print(f"\n🎤 Artistas de {pais} entre {inicio} y {fin}:")
    for artista in filtrados:
        print(f"- {artista['Artist name']} ({artista['Active years']})")

def artistas_por_genero(genero):
    """Muestra artistas de un género musical específico."""
    artistas = cargar_datos(ARTISTAS_JSON)
    
    filtrados = [artista for artista in artistas if genero.lower() in artista["Genre"].lower()]
    
    if not filtrados:
        print(f"⚠ No hay artistas en el género '{genero}'.")
        return

    print(f"\n🎵 Artistas en el género '{genero}':")
    for artista in filtrados:
        print(f"- {artista['Artist name']} ({artista['Country']})")

from datetime import datetime

def artistas_ultimos_10_años():
    """Obtiene artistas activos en los últimos 10 años."""
    artistas = cargar_datos(ARTISTAS_JSON)
    año_actual = datetime.now().year
    año_limite = año_actual - 10

    filtrados = [a for a in artistas if "present" in a["Active years"].lower() or int(a["Active years"].split("–")[-1]) >= año_limite]

    if not filtrados:
        print("⚠ No hay artistas activos en los últimos 10 años.")
        return

    print("\n🎶 Artistas activos en los últimos 10 años:")
    for artista in filtrados:
        print(f"- {artista['Artist name']} ({artista['Active years']})")

def contar_artistas_por_año():
    """Cuenta el número de artistas por año de primer éxito."""
    artistas = cargar_datos(ARTISTAS_JSON)
    conteo = {}

    for artista in artistas:
        año = artista["Release year of first charted record"]
        conteo[año] = conteo.get(año, 0) + 1

    print("\n📊 Número de artistas por año:")
    for año, cantidad in sorted(conteo.items()):
        print(f"{año}: {cantidad} artistas")

def unidades_certificadas_2023():
    """Calcula las unidades certificadas totales en 2023."""
    artistas = cargar_datos(ARTISTAS_JSON)
    total = sum(float(a["Total certified units"].split()[0]) for a in artistas)

    print(f"\n📀 Total de unidades certificadas en 2023: {total} millones")
