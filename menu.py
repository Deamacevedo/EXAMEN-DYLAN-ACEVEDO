from artistas import *
from paises import *
from generos import *
from reportes import *

menu_bienvenida="""
Bienvenido al portal usuario
1.Agregar Artista
2.Editar Artista
3.Eliminar Artista
4.Editar País
5.Eliminar País
6.Editar genero
7.Eliminar genero
8.Reporte: Artistas Últimos 10 Años
9.Reporte: Número de Artistas por Año
10.Reporte: Unidades Certificadas en 2023
11.Salir
"""

def menu_bienvenida_():
    print(menu_bienvenida)

def mostrar_menu():
    while True:
        menu_bienvenida()
   
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_artista()
            case "2":
                editar_artista()
            case "3":
                eliminar_artista()
            case "4":
                editar_pais()
            case "5":
                eliminar_pais()
            case "6":
                editar_genero()
            case "7":
                eliminar_genero()
            case "8":
                artistas_ultimos_10_años()
            case "9":
                artistas_por_pais_y_tiempo("United Kingdom", 1960, 1970)
            case "10":
                artistas_por_genero("Rock/pop")
            case "11":
                print("Saliendo del portal usuario")
                break
            case _:
                print("Digite una opcion correcta")


    mostrar_menu()