import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestWHR:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self): #¿Qué es self en python? Es como el this de java, es una referencia al objeto actual, se usa para acceder a los atributos y métodos de la clase desde dentro de la clase. En este caso, se usa para crear una instancia de HealthCalcImpl y asignarla a self.health_calc, lo que permite que cada test pueda usar esa instancia para llamar a los métodos de cálculo de salud.
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica WHR ---
    def test_whr_validos(self):
        """Cálculo de WHR con valores estándar válidos"""
        hip = 0.90
        waist = 0.70
        expected_whr = waist / hip
        assert self.health_calc.whr(waist, hip) == pytest.approx(expected_whr, abs=1e-5)

    def test_whr_extremos_validos(self):
        assert self.health_calc.whr(0.45, 0.45) == pytest.approx(1.0)
        assert self.health_calc.whr(3.0, 0.45) == pytest.approx(3.0 / 0.45)
        assert self.health_calc.whr(0.45, 3.0) == pytest.approx(0.45 / 3.0)


    def test_whr_cintura_0(self):
        """Lanzar excepción cuando el perímetro de la cintura es 0"""
        waist = 0
        hip = 0.90

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(waist, hip)


    def test_whr_cadera_0(self):
        """Lanzar excepción cuando el perímetro de la cadera es 0"""
        waist = 0.70
        hip = 0

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(waist, hip)

    def test_whr_negativos(self):
        """Lanzar excepción cuando los valores son negativos (Equivalente a assertAll)"""
        waist = -0.70
        hip = 0.90

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(waist, hip)

        waist = 0.70
        hip = -0.90
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(waist, hip)

    # --- Tests de Límites e Invalidación para el WHR ---
      @pytest.mark.parametrize("waist", [0.44, 3.01])
    def test_whr_cintura_fuera_rango(self, waist):
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(waist, 100.0)

    @pytest.mark.parametrize("hip", [0.44, 3.01])
    def test_whr_cadera_fuera_rango(self, hip):
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr(100.0, hip)



    # --- Tests de Clasificación básica a partir del WHR ---
    
    @pytest.mark.parametrize(
        "sex,whr,expected",
        [
            ("M", 0.90, "Pear"),
            ("M", 0.85, "Pear"),
            ("M", 0.91, "Apple"),
            ("M", 1.50, "Apple"),
            ("F", 0.85, "Pear"),
            ("F", 0.80, "Pear"),
            ("F", 0.86, "Apple"),
            ("F", 1.00, "Apple"),
        ],
        ids=lambda t: f"{t[0]} WHR={t[1]} -> {t[2]}",
    )
    def test_whr_classification_valida(self, sex: str, whr: float, expected: str):
        assert self.health_calc.whr_classification(sex, whr) == expected




    # --- Tests de Límites e Invalidación para la clasificación WHR ---

    @pytest.mark.parametrize("sex, whr", [("M", -0.85), ("F", -0.70), ("M", -0.90)], ids=lambda x: f"WHR negativo: {x}")
    def test_whr_classification_minimo_imposible(self, whr: float):
        """Lanzar excepción cuando el WHR es negativo."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr_classification(whr)

    @pytest.mark.parametrize("sex, whr", [1.01, 1.50, 2.00], ids=lambda x: f"WHR máximo extremo: {x}")
    def test_whr_classification_maximo_imposible(self, whr: float):
        """Lanzar excepción cuando el WHR es extremadamente alto."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr_classification(whr)

    @pytest.mark.parametrize("sex", ["X", "", "Male"], ids=lambda x: f"Sexo inválido: '{x}'")
    def test_whr_classification_sexo_invalido(self, sex: str):
        """Lanzar excepción cuando el sexo es inválido."""
        whr = 0.85

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.whr_classification(sex, whr)