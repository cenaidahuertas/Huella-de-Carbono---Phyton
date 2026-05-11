
from abc import ABC, abstractmethod

class HuellaCarbonoBase(ABC):

    @abstractmethod
    def calcular_huella(self):
        raise NotImplementedError(
        )

    @abstractmethod
    def get_info(self):
        raise NotImplementedError(
        )

    def mostrar_resultado(self):
        print("-" * 50)
        print(self.get_info())
        print("Huella de carbono: {:.2f} kg CO2/año".format(
            self.calcular_huella()
        ))
        print("-" * 50)

    def validar_valor_no_negativo(self, valor, nombre_campo):
        """Valida que un dato numerico no sea negativo."""
        if valor < 0:
            raise ValueError(
                "{} no puede ser negativo".format(nombre_campo)
            )
