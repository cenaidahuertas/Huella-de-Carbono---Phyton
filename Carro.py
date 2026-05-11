
from Huellacarbonobase import HuellaCarbonoBase


class Auto(HuellaCarbonoBase):
    FACTOR_GASOLINA = 2.31   # kg CO2 por litro
    FACTOR_DIESEL = 2.68     # kg CO2 por litro

    def __init__(self, marca, modelo, anio,
                km_anuales, rendimiento, tipo_combustible):
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
        return ("AUTO: {} {} {} | Combustible: {} | "
                "Km/año: {}").format(
                    self.anio, self.marca, self.modelo,
                    self.tipo_combustible.upper(), self.km_anuales
                )

    def __str__(self):
        return "Auto({} {} {}, {}, {} km/año)".format(
            self.anio, self.marca, self.modelo,
            self.tipo_combustible, self.km_anuales
        )
