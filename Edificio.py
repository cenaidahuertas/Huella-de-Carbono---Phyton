
from Huellacarbonobase import HuellaCarbonoBase

class Edificio(HuellaCarbonoBase):
    FACTOR_ELECTRICIDAD = 0.233   # kg CO2 por kWh
    FACTOR_GAS = 2.04             # kg CO2 por m3

    def __init__(self, nombre, direccion, num_pisos,
                kwh_electricidad, m3_gas, num_ocupantes):
        self.validar_valor_no_negativo(num_pisos, "num_pisos")
        self.validar_valor_no_negativo(
            kwh_electricidad, "kwh_electricidad"
        )
        self.validar_valor_no_negativo(m3_gas, "m3_gas")
        self.validar_valor_no_negativo(num_ocupantes, "num_ocupantes")
        self.nombre = nombre
        self.direccion = direccion
        self.num_pisos = num_pisos
        self.kwh_electricidad = kwh_electricidad
        self.m3_gas = m3_gas
        self.num_ocupantes = num_ocupantes

    def calcular_huella(self):
        emision_electricidad = self.kwh_electricidad * self.FACTOR_ELECTRICIDAD
        emision_gas = self.m3_gas * self.FACTOR_GAS
        return emision_electricidad + emision_gas

    def get_info(self):
        return ("EDIFICIO: {} | Direccion: {} | Pisos: {} | "
                "Ocupantes: {}").format(
                    self.nombre, self.direccion,
                    self.num_pisos, self.num_ocupantes
                )

    def __str__(self):
        return ("Edificio({}, {}, {} pisos, "
                "{} kWh/año, {} m3/año, {} ocupantes)").format(
                    self.nombre, self.direccion, self.num_pisos,
                    self.kwh_electricidad, self.m3_gas,
                    self.num_ocupantes
                )
