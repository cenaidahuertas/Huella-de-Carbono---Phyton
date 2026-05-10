# =============================================================
# manejador_archivos.py
# Modulo de manejo de archivos
# =============================================================
#
# MODULARIDAD:
#   Este modulo tiene UNA sola responsabilidad: guardar
#   y leer archivos. Segun el libro (Cap. 1.7.4 - Modules):
#   "A module is a Python source code file."
#   Separamos esta responsabilidad del programa principal
#   para que el codigo sea mas organizado y reutilizable.
#
# MANEJO DE ARCHIVOS:
#   Segun el libro Cap. 1.9.2 - File input and output:
#   Se usa open() con modos 'w' (escribir) y 'r' (leer).
#
# REUTILIZACION:
#   Cualquier otro programa puede importar este modulo
#   y usar guardar_reporte() sin reescribir nada.
# =============================================================

import os


def calcular_total_huella(lista_entidades):
    """
    Suma la huella total de una lista de entidades de manera polimorfica.
    """
    return sum(entidad.calcular_huella() for entidad in lista_entidades)


def guardar_reporte(lista_entidades, nombre_archivo="reporte_huella.txt"):
    """
    Guarda el reporte de huella de carbono en un archivo de texto.
    Segun libro Cap. 1.9.2 - File input and output.

    Args:
        lista_entidades (list): lista de objetos con calcular_huella()
        nombre_archivo (str): nombre del archivo de salida
    """
    # open() con 'w' crea o sobreescribe el archivo
    # encoding='utf-8' para soportar caracteres especiales
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=" * 55 + "\n")
        archivo.write("  REPORTE DE HUELLA DE CARBONO - POO PYTHON\n")
        archivo.write("  Cap. 1.8 - A Python Book (Kuhlman, 2013)\n")
        archivo.write("=" * 55 + "\n\n")

        total_co2 = 0
        numero = 1

        # Recorremos la lista de forma POLIMORFICA
        for entidad in lista_entidades:
            huella = entidad.calcular_huella()
            archivo.write("Entidad #{}\n".format(numero))
            archivo.write("Info   : {}\n".format(entidad.get_info()))
            archivo.write("Huella : {:.2f} kg CO2/anio\n".format(
                huella
            ))
            archivo.write("Detalle: {}\n".format(str(entidad)))
            archivo.write("-" * 55 + "\n")

            total_co2 += huella
            numero += 1

        archivo.write("\n")
        archivo.write("TOTAL CO2: {:.2f} kg/anio\n".format(total_co2))
        archivo.write("EQUIVALE : {:.4f} toneladas/anio\n".format(
            total_co2 / 1000
        ))
        archivo.write("=" * 55 + "\n")

        print("\n[OK] Reporte guardado en: {}".format(nombre_archivo))
    return total_co2


def leer_reporte(nombre_archivo="reporte_huella.txt"):
    """
    Lee e imprime el contenido del archivo de reporte.
    Segun libro Cap. 1.9.2 - File input and output.

    Args:
        nombre_archivo (str): nombre del archivo a leer
    """
    # Verificamos que el archivo exista
    if not os.path.exists(nombre_archivo):
        print("[AVISO] El archivo '{}' no existe.".format(nombre_archivo))
        return

    # open() con 'r' para leer
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        print("\n[LEYENDO ARCHIVO: {}]".format(nombre_archivo))
        print("=" * 55)
        for linea in archivo:
            print(linea, end="")
