# =============================================================
# edificio.py
# Clase Edificio
# =============================================================
#
# CONCEPTO POO - HERENCIA:
#   Edificio hereda de HuellaCarbonoBase.
#   Segun el libro (Cap. 1.8.6 - Adding inheritance):
#   "class B(A): ..." significa que B hereda de A.
#
# CONCEPTO POO - ENCAPSULAMIENTO:
#   Los atributos se definen en __init__ con self.
#   Se acceden con getters simples (Cap. 1.8.4).
#
# FORMULA HUELLA DE CARBONO EDIFICIO:
#   CO2 = (kwh_electricidad x 0.233) + (m3_gas x 2.04)
#   Fuente: EPA Greenhouse Gas Equivalencies Calculator
# =============================================================

from Huellacarbonobase import HuellaCarbonoBase


class Edificio(HuellaCarbonoBase):
    """
    Representa un edificio que consume electricidad y gas.
    Hereda de HuellaCarbonoBase e implementa calcular_huella().

    Atributos:
        nombre (str): nombre del edificio
        direccion (str): direccion del edificio
        num_pisos (int): numero de pisos
        kwh_electricidad (float): consumo electrico anual en kWh
        m3_gas (float): consumo de gas natural anual en m3
        num_ocupantes (int): cantidad de personas en el edificio
    """

    # -- Constantes de clase (compartidas por todos los edificios)
    # Segun libro Cap. 1.8.7 - Class variables
    FACTOR_ELECTRICIDAD = 0.233   # kg CO2 por kWh
    FACTOR_GAS = 2.04             # kg CO2 por m3

    def __init__(self, nombre, direccion, num_pisos,
                 kwh_electricidad, m3_gas, num_ocupantes):
        """
        Constructor del Edificio.
        Segun libro Cap. 1.8.3 - The constructor.

        Args:
            nombre (str): nombre del edificio
            direccion (str): direccion del edificio
            num_pisos (int): numero de pisos
            kwh_electricidad (float): consumo electrico en kWh/anio
            m3_gas (float): consumo de gas en m3/anio
            num_ocupantes (int): numero de ocupantes
        """
        # self guarda el estado de cada objeto (Cap. 1.8.3)
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
        """
        POLIMORFISMO: implementacion especifica para edificios.
        Formula: CO2 = (kWh x 0.233) + (m3 x 2.04)

        Returns:
            float: kg de CO2 emitidos por el edificio al anio
        """
        emision_electricidad = self.kwh_electricidad * self.FACTOR_ELECTRICIDAD
        emision_gas = self.m3_gas * self.FACTOR_GAS
        return emision_electricidad + emision_gas

    def get_info(self):
        """
        Retorna descripcion del edificio.

        Returns:
            str: informacion del edificio
        """
        return ("EDIFICIO: {} | Direccion: {} | Pisos: {} | "
                "Ocupantes: {}").format(
                    self.nombre, self.direccion,
                    self.num_pisos, self.num_ocupantes
                )

    def __str__(self):
        """
        Representacion en texto del objeto.
        Segun libro Cap. 1.9.1 - __str__() method.
        """
        return ("Edificio({}, {}, {} pisos, "
                "{} kWh/anio, {} m3/anio, {} ocupantes)").format(
                    self.nombre, self.direccion, self.num_pisos,
                    self.kwh_electricidad, self.m3_gas,
                    self.num_ocupantes
                )
