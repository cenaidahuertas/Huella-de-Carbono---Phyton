
from Huellacarbonobase import HuellaCarbonoBase

class Bicicleta(HuellaCarbonoBase):
    """
    Representa una bicicleta con huella de carbono de fabricacion.
    Hereda de HuellaCarbonoBase e implementa calcular_huella().

    Atributos:
        propietario (str): nombre del duenio
        marca (str): marca de la bicicleta
        tipo (str): tipo de bicicleta (urbana, montana, ruta)
        km_anuales (float): km recorridos al año
        anios_vida_util (int): cuantos años dura la bicicleta
        co2_fabricacion (float): kg CO2 emitidos al fabricarla
        costo_mantenimiento (float): USD gastados en mant/año
    """

    FACTOR_MANTENIMIENTO = 0.5   # kg CO2 por USD gastado

    def __init__(self, propietario, marca, tipo,
                km_anuales, anios_vida_util,
                co2_fabricacion, costo_mantenimiento):
        """
        Constructor de la Bicicleta.

        Args:
            propietario (str): duenio de la bicicleta
            marca (str): marca de la bicicleta
            tipo (str): tipo (urbana, montana, ruta, electrica)
            km_anuales (float): km recorridos por año
            anios_vida_util (int): años de vida util estimados
            co2_fabricacion (float): kg CO2 de su fabricacion
            costo_mantenimiento (float): USD de mantenimiento/año
        """
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
        """
        POLIMORFISMO: implementacion especifica para bicicletas.
        Calcula la huella de fabricacion amortizada + mantenimiento.

        Returns:
            float: kg de CO2 anuales de la bicicleta
        """
        amortizacion = self.co2_fabricacion / self.anios_vida_util
        emision_mantenimiento = (self.costo_mantenimiento
                                 * self.FACTOR_MANTENIMIENTO)
        return amortizacion + emision_mantenimiento

    def get_info(self):
        """
        Retorna descripcion de la bicicleta.

        Returns:
            str: informacion de la bicicleta
        """
        return ("BICICLETA: {} {} | Propietario: {} | "
                "Tipo: {} | Km/año: {}").format(
                    self.marca, self.tipo, self.propietario,
                    self.tipo.upper(), self.km_anuales
                )

    def __str__(self):
        """Representacion en texto del objeto."""
        return "Bicicleta({} {}, propietario: {}, {} km/año)".format(
            self.marca, self.tipo, self.propietario, self.km_anuales
        )
