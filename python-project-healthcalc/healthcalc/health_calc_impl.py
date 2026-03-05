from healthcalc import HealthCalc, InvalidHealthDataException


class HealthCalcImpl(HealthCalc):

    def bmi_classification(self, bmi: float) -> str:
        if bmi < 0:
            raise InvalidHealthDataException("BMI cannot be negative.")
        if bmi > 150:
            raise InvalidHealthDataException("BMI must be within a possible biological range [0-150].")
        
        result = "Obesity"
        if bmi < 18.5:
            result = "Underweight"
        elif bmi < 25:
            result = "Normal weight"
        elif bmi < 30:
            result = "Overweight"
        return result

    def bmi(self, weight: float, height: float) -> float:
        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")
        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if weight < 1 or weight > 700:
            raise InvalidHealthDataException("Weight must be within a possible biological range [1-700] kg.")
        if height < 0.30 or height > 3.00:
            raise InvalidHealthDataException("Height must be within a possible biological range [0.30-3.00] m.")
            
        return weight / (height ** 2)


    def lorentz(self, sex: str, height: float) -> float:
        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if height < 1.00 or height > 3.00:
            raise InvalidHealthDataException("Height must be within a possible biological range [1.00-3.00] m.")
        if sex.upper() != "M" and sex.upper() != "F":
            raise InvalidHealthDataException("Sex must be either 'M' (Male) or 'F' (Female).")

        if sex.upper() == "M":
            return (height*100 - 100) - ((height*100 - 150)/4)
        else:
            return (height*100 - 100) - ((height*100 - 150)/2)
        
    def whr(self, waist:float, hip:float) -> float:
        if waist <= 0:
            raise InvalidHealthDataException("Waist perimeter must be positive.")
        if hip <= 0:
            raise InvalidHealthDataException("Hip perimeter must be positive.")
        if waist < 0.45 or waist > 3.00:
            raise InvalidHealthDataException("Waist perimeter must be within a possible biological range [0.45-3.00] m.")
        if hip < 0.45 or hip > 3.00:
            raise InvalidHealthDataException("Hip perimeter must be within a possible biological range [0.45-3.00] m.")

        return waist/hip
    
    def whr_classification(self, sex: str, whr: float) -> str:
        if whr < 0:
            raise InvalidHealthDataException("WHR cannot be negative.")
        if whr > 5:
            raise InvalidHealthDataException("WHR must be within a possible biological range [0-5].")
        if sex.upper() != "M" and sex.upper() != "F":
            raise InvalidHealthDataException("Sex must be either 'M' (Male) or 'F' (Female).")

        result = "Apple"
        if sex.upper() == "M":
            if whr <= 0.90:
                result = "Pear"
        else:
            if whr <= 0.85:
                result = "Pear"
            
        return result


