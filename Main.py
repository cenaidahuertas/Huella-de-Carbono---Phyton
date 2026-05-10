
from Edificio import Edificio
from Carro import Auto
from Bicicleta import Bicicleta
from Manejadorarchivos import (
    calcular_total_huella,
    guardar_reporte,
    leer_reporte,
)


def main():
    """Funcion principal del programa."""

    print("=" * 55)
    print("  HUELLA DE CARBONO - POO PYTHON")
    print("  Basado en Cap. 1.8 - A Python Book")
    print("=" * 55)

    # ──────────────────────────────────────────────────────
    # PASO 1: Crear objetos de cada clase
    #
    # Cada clase tiene atributos DIFERENTES.
    # No hay herencia entre Edificio, Auto y Bicicleta.
    # Lo que comparten es la clase base HuellaCarbonoBase.
    # ──────────────────────────────────────────────────────

    # -- Edificios --
    edificio1 = Edificio(
        nombre="Torre Norte",
        direccion="Calle 100 #15-30, Bogota",
        num_pisos=20,
        kwh_electricidad=450000,   # kWh al año
        m3_gas=12000,              # m3 de gas al año
        num_ocupantes=850
    )

    edificio2 = Edificio(
        nombre="Casa Familiar",
        direccion="Carrera 45 #72-18, Medellin",
        num_pisos=2,
        kwh_electricidad=3600,
        m3_gas=800,
        num_ocupantes=4
    )

    # -- Autos --
    auto1 = Auto(
        marca="Toyota",
        modelo="Corolla",
        anio=2021,
        km_anuales=18000,
        rendimiento=13.5,          # km por litro
        tipo_combustible="gasolina"
    )

    auto2 = Auto(
        marca="Ford",
        modelo="Ranger",
        anio=2019,
        km_anuales=25000,
        rendimiento=9.0,
        tipo_combustible="diesel"
    )

    auto3 = Auto(
        marca="Tesla",
        modelo="Model 3",
        anio=2023,
        km_anuales=20000,
        rendimiento=0,             # no aplica
        tipo_combustible="electrico"
    )

    # -- Bicicletas --
    bici1 = Bicicleta(
        propietario="Carlos Rodriguez",
        marca="Trek",
        tipo="urbana",
        km_anuales=3500,
        anios_vida_util=10,
        co2_fabricacion=96.0,     # kg CO2 de fabricacion
        costo_mantenimiento=50.0  # USD al año
    )

    bici2 = Bicicleta(
        propietario="Laura Gomez",
        marca="Specialized",
        tipo="electrica",
        km_anuales=5000,
        anios_vida_util=8,
        co2_fabricacion=134.0,
        costo_mantenimiento=80.0
    )

    # ──────────────────────────────────────────────────────
    # PASO 2: Guardar todos en una lista
    # la lista guarda objetos de distintos tipos.
    # Todos comparten la clase base HuellaCarbonoBase.
    # Python no necesita declarar el tipo de la lista.
    # ──────────────────────────────────────────────────────

    entidades = [
        edificio1, edificio2,
        auto1, auto2, auto3,
        bici1, bici2
    ]

    print("\nTotal de entidades: {}".format(len(entidades)))

    # ──────────────────────────────────────────────────────
    # 
    # El for llama a calcular_huella() en cada objeto.
    # Python decide en tiempo de ejecucion cual usar:
    #   - Si es Edificio    → formula kWh y gas
    #   - Si es Auto        → formula litros x factor
    #   - Si es Bicicleta   → formula fabricacion
    #
    # 
    # ──────────────────────────────────────────────────────

    print("\n--- RESULTADOS DE HUELLA DE CARBONO ---\n")

    for entidad in entidades:
        # mostrar_resultado() es heredado de HuellaCarbonoBase
        entidad.mostrar_resultado()

    total_co2 = calcular_total_huella(entidades)

    # ──────────────────────────────────────────────────────
    # PASO 4: Mostrar resumen
    # ──────────────────────────────────────────────────────

    print("\n" + "=" * 55)
    print("  RESUMEN FINAL")
    print("=" * 55)
    print("  Entidades procesadas : {}".format(len(entidades)))
    print("  Total CO2            : {:.2f} kg/año".format(total_co2))
    print("  Equivale a           : {:.4f} toneladas/año".format(
        total_co2 / 1000
    ))
    print("=" * 55)

    # ──────────────────────────────────────────────────────
    # PASO 5: Guardar en archivo de texto
    # (modulo externo - MODULARIDAD)
    # ──────────────────────────────────────────────────────

    print("\n--- GUARDANDO REPORTE EN ARCHIVO ---")
    guardar_reporte(entidades)

    # Leemos el archivo para verificar que se guardo
    leer_reporte()


# Segun libro Cap. 1.7.4 - idioma para modulos ejecutables
if __name__ == "__main__":
    main()
