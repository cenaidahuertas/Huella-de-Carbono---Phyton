
from Huellacarbonobase import HuellaCarbonoBase


class Auto(HuellaCarbonoBase):
    """
    Representa un automovil que consume combustible.
    Hereda de HuellaCarbonoBase e implementa calcular_huella().

    Atributos:
        marca (str): marca del vehiculo
        modelo (str): modelo del vehiculo
        anio (int): año de fabricacion
        km_anuales (float): kilometros recorridos al año
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
            anio (int): año de fabricacion
            km_anuales (float): km recorridos por año
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
        self.tipo_combustible = tipo_combustible.lower()

    def calcular_huella(self):
        """

        Returns:
            float: kg de CO2 emitidos por el auto al año
        """
        # Autos electricos no emiten CO2 directamente
        if self.tipo_combustible == "electrico":
            return 0.0

        # Calculamos litros consumidos en el año
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
                "Km/año: {}").format(
                    self.anio, self.marca, self.modelo,
                    self.tipo_combustible.upper(), self.km_anuales
                )

    def __str__(self):
        """Representacion en texto del objeto."""
        return "Auto({} {} {}, {}, {} km/año)".format(
            self.anio, self.marca, self.modelo,
            self.tipo_combustible, self.km_anuales
        )
