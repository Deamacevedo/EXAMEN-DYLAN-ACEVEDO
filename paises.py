from archivo_json import cargar_datos, guardar_datos

PAISES_JSON = "data/paises.json"

def agregar_pais():
    paises = cargar_datos(PAISES_JSON)

    nombre = input("Nombre del país: ").strip()
    iso = input("Código ISO (2 letras): ").strip().upper()
    iso3 = input("Código ISO3 (3 letras): ").strip().upper()

    nuevo_pais = {"Country": nombre, "ISO": iso, "ISO3": iso3}

    paises.append(nuevo_pais)
    guardar_datos(PAISES_JSON, paises)
    print("País agregado correctamente.")

def mostrar_paises():
    paises = cargar_datos(PAISES_JSON)
    
    if not paises:
        print("⚠ No hay países registrados.")
        return

    print("\n🌍 Lista de Países:")
    for pais in paises:
        print(f"- {pais['Country']} (ISO: {pais['ISO']}, ISO3: {pais['ISO3']})")

def editar_pais():
    paises = cargar_datos(PAISES_JSON)

    nombre = input("Ingrese el nombre del país a editar: ").strip()
    pais = next((p for p in paises if p["Country"].lower() == nombre.lower()), None)

    if not pais:
        print("País no encontrado.")
        return

    pais["ISO"] = input(f"Nuevo código ISO ({pais['ISO']}): ").strip().upper() or pais["ISO"]
    pais["ISO3"] = input(f"Nuevo código ISO3 ({pais['ISO3']}): ").strip().upper() or pais["ISO3"]

    guardar_datos(PAISES_JSON, paises)
    print("País editado correctamente.")

def eliminar_pais():
    paises = cargar_datos(PAISES_JSON)

    nombre = input("Ingrese el nombre del país a eliminar: ").strip()
    paises_filtrados = [p for p in paises if p["Country"].lower() != nombre.lower()]

    if len(paises) == len(paises_filtrados):
        print("País no encontrado.")
        return

    guardar_datos(PAISES_JSON, paises_filtrados)
    print("País eliminado correctamente.")
