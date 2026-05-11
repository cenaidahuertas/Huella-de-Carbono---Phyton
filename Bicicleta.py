
from Huellacarbonobase import HuellaCarbonoBase

class Bicicleta(HuellaCarbonoBase):
    FACTOR_MANTENIMIENTO = 0.5   # kg CO2 por USD gastado

    def __init__(self, propietario, marca, tipo,
                km_anuales, anios_vida_util,
                co2_fabricacion, costo_mantenimiento):
        self.validar_valor_no_negativo(km_anuales, "km_anuales")
        if anios_vida_util <= 0:
            raise ValueError("años de vida util debe ser mayor que cero")
        self.validar_valor_no_negativo(
            co2_fabricacion, "co2_fabricacion"
        )
        self.validar_valor_no_negativo(
            costo_mantenimiento, "costo_mantenimiento"
        )
        self.propietario = propietario
        self.marca = marca
        self.tipo = tipo
        self.km_anuales = km_anuales
        self.anios_vida_util = anios_vida_util
        self.co2_fabricacion = co2_fabricacion
        self.costo_mantenimiento = costo_mantenimiento

    def calcular_huella(self):
        amortizacion = self.co2_fabricacion / self.anios_vida_util
        emision_mantenimiento = (self.costo_mantenimiento
                                 * self.FACTOR_MANTENIMIENTO)
        return amortizacion + emision_mantenimiento

    def get_info(self):
        return ("BICICLETA: {} {} | Propietario: {} | "
                "Tipo: {} | Km/año: {}").format(
                    self.marca, self.tipo, self.propietario,
                    self.tipo.upper(), self.km_anuales
                )

    def __str__(self):
        return "Bicicleta({} {}, propietario: {}, {} km/año)".format(
            self.marca, self.tipo, self.propietario, self.km_anuales
        )
