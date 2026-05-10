
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from Bicicleta import Bicicleta
from Carro import Auto
from Edificio import Edificio
from Manejadorarchivos import calcular_total_huella, guardar_reporte


# =============================================================
# PRUEBAS PARA LA CLASE EDIFICIO
# =============================================================

class TestEdificio(unittest.TestCase):
    """
    Pruebas unitarias para la clase Edificio.
    Hereda de unittest.TestCase (Cap. 1.9.3 del libro).
    """

    def setUp(self):
        """
        setUp() se ejecuta ANTES de cada test.
        Segun libro: "instance methods setUp and tearDown are
        run automatically before each and after each test."
        Creamos un edificio de prueba con valores conocidos.
        """
        # 10000 kWh x 0.233 = 2330.0 kg CO2
        # 1000 m3  x 2.04  = 2040.0 kg CO2
        # Total esperado     = 4370.0 kg CO2/año
        self.edificio = Edificio(
            nombre="Edificio Test",
            direccion="Bogota",
            num_pisos=5,
            kwh_electricidad=10000,
            m3_gas=1000,
            num_ocupantes=50
        )

    def test_huella_total_correcta(self):
        """
        La huella total debe ser 4370.0 kg CO2/año.
        10000 x 0.233 + 1000 x 2.04 = 2330 + 2040 = 4370
        """
        # ARRANGE: ya en setUp
        esperado = 4370.0

        # ACT
        resultado = self.edificio.calcular_huella()

        # ASSERT
        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="La huella del edificio debe ser 4370 kg CO2/año")

    def test_huella_solo_electricidad(self):
        """Sin gas, la huella es solo kWh x 0.233."""
        self.edificio.m3_gas = 0
        esperado = 10000 * 0.233  # 2330.0

        resultado = self.edificio.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="Sin gas, la huella debe ser solo electricidad")

    def test_huella_solo_gas(self):
        """Sin electricidad, la huella es solo m3 x 2.04."""
        self.edificio.kwh_electricidad = 0
        esperado = 1000 * 2.04  # 2040.0

        resultado = self.edificio.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="Sin electricidad, la huella debe ser solo gas")

    def test_huella_cero_sin_consumo(self):
        """Sin consumo, la huella debe ser 0."""
        self.edificio.kwh_electricidad = 0
        self.edificio.m3_gas = 0

        self.assertEqual(self.edificio.calcular_huella(), 0.0,
            msg="Sin consumo la huella debe ser 0")

    def test_get_info_no_es_vacio(self):
        """get_info() debe retornar texto con el nombre."""
        info = self.edificio.get_info()

        self.assertIsNotNone(info,
            msg="get_info no debe retornar None")
        self.assertIn("Edificio Test", info,
            msg="get_info debe incluir el nombre del edificio")

    def test_mas_consumo_mas_huella(self):
        """Duplicar el consumo electrico debe aumentar la huella."""
        huella_original = self.edificio.calcular_huella()
        self.edificio.kwh_electricidad = 20000  # doble

        self.assertGreater(self.edificio.calcular_huella(),
                           huella_original,
            msg="Mayor consumo debe producir mayor huella")


# =============================================================
# PRUEBAS PARA LA CLASE AUTO
# =============================================================

class TestAuto(unittest.TestCase):
    """Pruebas unitarias para la clase Auto."""

    def setUp(self):
        """
        Creamos tres autos de prueba: gasolina, diesel, electrico.
        Con 10 km/L y 10000 km/año → consumen 1000 litros.
        """
        self.auto_gasolina = Auto(
            marca="Toyota", modelo="Corolla", anio=2020,
            km_anuales=10000,
            rendimiento=10.0,  # 10000/10 = 1000 litros
            tipo_combustible="gasolina"
        )
        # 1000 litros x 2.31 = 2310.0 kg CO2

        self.auto_diesel = Auto(
            marca="Ford", modelo="Ranger", anio=2019,
            km_anuales=10000,
            rendimiento=10.0,
            tipo_combustible="diesel"
        )
        # 1000 litros x 2.68 = 2680.0 kg CO2

        self.auto_electrico = Auto(
            marca="Tesla", modelo="Model 3", anio=2023,
            km_anuales=20000,
            rendimiento=0,
            tipo_combustible="electrico"
        )

    def test_huella_gasolina(self):
        """10000km / 10km/L x 2.31 = 2310 kg CO2."""
        esperado = 2310.0

        resultado = self.auto_gasolina.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="Auto gasolina debe ser 2310 kg CO2/año")

    def test_huella_diesel(self):
        """10000km / 10km/L x 2.68 = 2680 kg CO2."""
        esperado = 2680.0

        resultado = self.auto_diesel.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="Auto diesel debe ser 2680 kg CO2/año")

    def test_huella_electrico_es_cero(self):
        """Auto electrico no emite CO2 directamente."""
        self.assertEqual(self.auto_electrico.calcular_huella(), 0.0,
            msg="Auto electrico debe tener huella = 0")

    def test_diesel_mayor_que_gasolina(self):
        """El diesel emite mas CO2 que la gasolina."""
        self.assertGreater(
            self.auto_diesel.calcular_huella(),
            self.auto_gasolina.calcular_huella(),
            msg="Diesel debe tener mayor huella que gasolina"
        )

    def test_mas_km_mas_huella(self):
        """A mayor kilometraje, mayor huella."""
        huella_original = self.auto_gasolina.calcular_huella()
        self.auto_gasolina.km_anuales = 20000  # doble de km

        self.assertGreater(self.auto_gasolina.calcular_huella(),
                           huella_original,
            msg="Mas km debe producir mayor huella")

    def test_combustible_en_minusculas(self):
        """El tipo de combustible se guarda en minusculas."""
        auto = Auto("Honda", "Civic", 2022, 15000, 12.0, "GASOLINA")

        self.assertEqual(auto.tipo_combustible, "gasolina",
            msg="tipo_combustible debe guardarse en minusculas")

    def test_get_info_contiene_marca(self):
        """get_info() debe contener la marca del auto."""
        info = self.auto_gasolina.get_info()

        self.assertIn("Toyota", info,
            msg="get_info debe incluir la marca del auto")

    def test_rendimiento_invalido_lanza_error(self):
        """Un auto no electrico no debe aceptar rendimiento 0."""
        with self.assertRaises(ValueError):
            Auto("Mazda", "3", 2024, 12000, 0, "gasolina")


# =============================================================
# PRUEBAS PARA LA CLASE BICICLETA
# =============================================================

class TestBicicleta(unittest.TestCase):
    """Pruebas unitarias para la clase Bicicleta."""

    def setUp(self):
        """
        Bicicleta de prueba con valores conocidos:
        co2_fabricacion=100, vida_util=10 → amort = 10/año
        costo_mantenimiento=50, factor=0.5 → emision = 25/año
        Total esperado = 35.0 kg CO2/año
        """
        self.bici = Bicicleta(
            propietario="Ana Torres",
            marca="Trek",
            tipo="urbana",
            km_anuales=3000,
            anios_vida_util=10,
            co2_fabricacion=100.0,
            costo_mantenimiento=50.0
        )

    def test_huella_total_correcta(self):
        """100/10 + 50 x 0.5 = 10 + 25 = 35 kg CO2/año."""
        esperado = 35.0

        resultado = self.bici.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="La huella de la bici debe ser 35 kg CO2/año")

    def test_sin_mantenimiento_solo_amortizacion(self):
        """Sin mantenimiento, la huella es solo amortizacion."""
        self.bici.costo_mantenimiento = 0
        esperado = 100.0 / 10  # = 10.0

        resultado = self.bici.calcular_huella()

        self.assertAlmostEqual(resultado, esperado, places=1,
            msg="Sin mantenimiento, huella = co2_fab / vida_util")

    def test_mayor_vida_util_menor_huella(self):
        """Mayor vida util reduce la amortizacion anual."""
        huella_10 = self.bici.calcular_huella()  # vida=10
        self.bici.anios_vida_util = 20            # vida=20

        self.assertLess(self.bici.calcular_huella(), huella_10,
            msg="Mayor vida util debe reducir la huella anual")

    def test_get_info_tiene_propietario(self):
        """get_info() debe incluir el nombre del propietario."""
        info = self.bici.get_info()

        self.assertIn("Ana Torres", info,
            msg="get_info debe incluir el nombre del propietario")

    def test_str_tiene_marca(self):
        """str(bici) debe incluir la marca."""
        texto = str(self.bici)

        self.assertIn("Trek", texto,
            msg="str() debe incluir la marca de la bicicleta")

    def test_vida_util_invalida_lanza_error(self):
        """La vida util debe ser mayor que cero."""
        with self.assertRaises(ValueError):
            Bicicleta(
                propietario="Ana Torres",
                marca="Trek",
                tipo="urbana",
                km_anuales=3000,
                anios_vida_util=0,
                co2_fabricacion=100.0,
                costo_mantenimiento=50.0
            )


# =============================================================
# PRUEBAS PARA MODULARIDAD Y MANEJO DE ARCHIVOS
# =============================================================

class TestManejadorArchivos(unittest.TestCase):
    """Pruebas del modulo de archivos y calculo reutilizable."""

    def setUp(self):
        self.entidades = [
            Edificio("Prueba", "Bogota", 2, 1000, 100, 8),
            Auto("Renault", "Logan", 2020, 10000, 10, "gasolina"),
            Bicicleta("Luis", "GW", "urbana", 1500, 10, 80, 20),
        ]

    def test_calcular_total_huella_retorna_suma_esperada(self):
        """La suma debe coincidir con el calculo individual."""
        esperado = sum(
            entidad.calcular_huella()
            for entidad in self.entidades
        )
        self.assertAlmostEqual(
            calcular_total_huella(self.entidades),
            esperado,
            places=2
        )

    def test_guardar_reporte_crea_archivo_con_total(self):
        """El reporte debe escribirse correctamente en disco."""
        with TemporaryDirectory() as carpeta_temporal:
            ruta = Path(carpeta_temporal) / "reporte_prueba.txt"
            total = guardar_reporte(self.entidades, str(ruta))
            existe_archivo = ruta.exists()
            contenido = ruta.read_text(encoding="utf-8")

        self.assertTrue(existe_archivo)
        self.assertGreaterEqual(total, 0)
        self.assertIn("REPORTE DE HUELLA DE CARBONO", contenido)
        self.assertIn("TOTAL CO2", contenido)


# =============================================================
# Ejecutar las pruebas
# Segun libro Cap. 1.9.3.1 - A simple example
# =============================================================

def main():
    """Ejecuta todas las pruebas con reporte detallado."""
    print("=" * 55)
    print("  PRUEBAS UNITARIAS - HUELLA DE CARBONO")
    print("  unittest - Cap. 1.9.3 Python Book")
    print("=" * 55)
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
