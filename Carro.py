# =============================================================
# auto.py
# Clase Auto
# =============================================================
#
# HERENCIA: Auto hereda de HuellaCarbonoBase.
# POLIMORFISMO: calcular_huella() usa formula de combustible.
#
# FORMULA HUELLA DE CARBONO AUTO:
#   litros = km_anuales / rendimiento_km_por_litro
#   CO2    = litros x factor_combustible
#
#   Factor gasolina : 2.31 kg CO2/litro
#   Factor diesel   : 2.68 kg CO2/litro
#   Electrico       : 0.0  (no emite CO2 directo)
# =============================================================

from Huellacarbonobase import HuellaCarbonoBase


class Auto(HuellaCarbonoBase):
    """
    Representa un automovil que consume combustible.
    Hereda de HuellaCarbonoBase e implementa calcular_huella().

    Atributos:
        marca (str): marca del vehiculo
        modelo (str): modelo del vehiculo
        anio (int): anio de fabricacion
        km_anuales (float): kilometros recorridos al anio
        rendimiento (float): km por litro de combustible
        tipo_combustible (str): 'gasolina', 'diesel' o 'electrico'
    """

    # Factores de emision por tipo de combustible (Cap. 1.8.7)
    FACTOR_GASOLINA = 2.31   # kg CO2 por litro
    FACTOR_DIESEL = 2.68     # kg CO2 por litro

    def __init__(self, marca, modelo, anio,
                 km_anuales, rendimiento, tipo_combustible):
        """
        Constructor del Auto.

        Args:
            marca (str): marca del vehiculo
            modelo (str): modelo del vehiculo
            anio (int): anio de fabricacion
            km_anuales (float): km recorridos por anio
            rendimiento (float): km que rinde por litro
            tipo_combustible (str): 'gasolina', 'diesel' o 'electrico'
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.validar_valor_no_negativo(km_anuales, "km_anuales")
        if tipo_combustible.lower() != "electrico":
            if rendimiento <= 0:
                raise ValueError(
                    "rendimiento debe ser mayor que cero"
                )
        else:
            self.validar_valor_no_negativo(rendimiento, "rendimiento")
        self.km_anuales = km_anuales
        self.rendimiento = rendimiento
        # Guardamos en minusculas para evitar errores
        self.tipo_combustible = tipo_combustible.lower()

    def calcular_huella(self):
        """
        POLIMORFISMO: implementacion especifica para autos.
        Los autos electricos tienen huella directa de 0.

        Returns:
            float: kg de CO2 emitidos por el auto al anio
        """
        # Autos electricos no emiten CO2 directamente
        if self.tipo_combustible == "electrico":
            return 0.0

        # Calculamos litros consumidos en el anio
        litros_consumidos = self.km_anuales / self.rendimiento

        # Elegimos el factor segun el combustible
        if self.tipo_combustible == "diesel":
            factor = self.FACTOR_DIESEL
        else:
            factor = self.FACTOR_GASOLINA

        return litros_consumidos * factor

    def get_info(self):
        """
        Retorna descripcion del auto.

        Returns:
            str: informacion del auto
        """
        return ("AUTO: {} {} {} | Combustible: {} | "
                "Km/anio: {}").format(
                    self.anio, self.marca, self.modelo,
                    self.tipo_combustible.upper(), self.km_anuales
                )

    def __str__(self):
        """Representacion en texto del objeto."""
        return "Auto({} {} {}, {}, {} km/anio)".format(
            self.anio, self.marca, self.modelo,
            self.tipo_combustible, self.km_anuales
        )
