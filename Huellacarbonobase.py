

from abc import ABC, abstractmethod


class HuellaCarbonoBase(ABC):
    """
    Clase base que define el contrato para calcular
    la huella de carbono de cualquier entidad.

    Todas las clases que hereden de esta deben
    implementar los metodos calcular_huella() y get_info().
    """

    @abstractmethod
    def calcular_huella(self):
        """
        Calcula la huella de carbono anual en kg de CO2.
        DEBE ser implementado por cada subclase.
        """
        raise NotImplementedError(
            "La subclase debe implementar calcular_huella()"
        )

    @abstractmethod
    def get_info(self):
        """
        Retorna informacion del objeto para el reporte.
        DEBE ser implementado por cada subclase.
        """
        raise NotImplementedError(
            "La subclase debe implementar get_info()"
        )

    def mostrar_resultado(self):
        """
        REUTILIZACION DE CODIGO:
        Este metodo es heredado por TODAS las subclases.
        Ninguna necesita volver a escribirlo.
        Llama a calcular_huella() que cada una define diferente.
        """
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
