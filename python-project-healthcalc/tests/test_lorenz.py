import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestBMI:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica IBW ---
    def test_lorentz_valido_hombre(self):
        """Cálculo de IBW con valores estándar válidos para hombres"""
        
        height = 1.75
        expected_lorentz = (height*100-100) - ((height*100 -150)/4)

        result = self.health_calc.lorentz("M", height)

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_lorentz, abs=0.01)
    
    def test_lorentz_valido_mujer(self):
        """Cálculo de IBW con valores estándar válidos para mujeres"""
        
        height = 1.75
        expected_lorentz = (height*100-100) - ((height*100 -150)/2)

        result = self.health_calc.lorentz("F", height)

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_lorentz, abs=0.01)

    def test_lorentz_altura_cero(self):
        """Lanzar excepción cuando la altura es cero"""
        sex = "M"
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(sex, 0)

    def test_lorentz_negativos(self):
        """Lanzar excepción cuando los valores son negativos (Equivalente a assertAll)"""
        sex = "F"
        height = -1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(sex, height)

    # --- Tests de Límites e Invalidación para el IBW ---
    @pytest.mark.parametrize("height", [-0.50, 0.0, 0.99], ids=lambda x: f"Altura mínima inválida: {x}m")
    def test_altura_minima_imposible(self, height: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        sex = "F"
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(sex, height)

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        sex = "M"
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(sex, height)
    

    @pytest.mark.parametrize("sex", ["X", ".", "h", "", "AB", "1", " "], ids=lambda x: f"Sexo inválido: {x!r}")
    def test_lorentz_sexo_invalido(self, sex: str):
        """Lanzar excepción cuando el sexo no es 'M' ni 'F'."""
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.lorentz(sex, height)