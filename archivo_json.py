import json
import os

def cargar_datos(nombre_archivo):
    """Carga datos desde un archivo JSON o retorna una lista vacía si no existe."""
    if not os.path.exists(nombre_archivo):
        return []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(nombre_archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
