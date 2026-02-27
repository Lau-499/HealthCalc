# HealthCalc
Bienvenido al proyecto de la asignatura de **Ingeniería del Software Avanzada**.

El [Hospital Universitario Virgen de la Victoria (El Clínico)](https://www.sspa.juntadeandalucia.es/servicioandaluzdesalud/hospital/virgen-victoria/) de Málaga nos ha encargado el desarrollo de una **Calculadora de Salud** (**_HealthCalc_**) que permita calcular diferentes métricas de los pacientes.

![MOdelo de características de la calculadora de salud.](resources/images/healthcalc_fm.png)

## Requisitos  

<details>
<summary><b>Requisitos Funcionales</b></summary>

- La calculadora debe dar soporte a al menos tres métricas.

</details>

<details>
<summary><b>Requisitos No Funcionales</b></summary>

Para que el proyecto cumpla con estándares de software médico, se deben incluir:
- **Gestión de Errores:** Manejo de excepciones en divisiones por cero (ej. altura 0 en IMC).
  1.  **Validación de Rangos (_Data Scrubbing_):**
      * *Hard Limits:* Bloquear entradas imposibles (ej. altura de 4 metros).
      * *Soft Limits:* Avisos ante valores inusuales pero posibles.
    
        > **Límites Biológicos Reales**:
            * **Altura:** El ser humano más alto registrado midió aproximadamente 272 cm. Un límite de 300 cm es un "Hard Limit" sensato.
            Un recién nacido puede medir 40cm. Un límite inferior sensato es de 30cm.
            * **Peso:** El peso máximo registrado ronda los 635 kg. Un límite de 700 kg sería el tope lógico.
            Un recién nacido puede pesar 2kg. Un límite inferior sensato es de 1kg.
  2.  **Soporte Multi-unidad:** Conversión automática entre sistema métrico (kg, cm) e imperial (lb, ft/in).
  3.  **Gestión de Errores:** Manejo de excepciones en divisiones por cero (ej. altura 0 en IMC).
- Todo el código de la aplicación (incluido los comentarios) deben estar en inglés.
- **Privacidad (_Compliance_):** Si el software almacena datos, debe considerar la anonimización de la Información Personal Identificable (PII) bajo normativas como GDPR o HIPAA.

</details>



## Métricas de HealthCalc

<details>
<summary><b>Métricas Antropométricas</b></summary>

* **M1: Índice de Masa Corporal (IMC) o _Body Mass Index (BMI)_:** El IMC es es un indicador estándar, adoptado por la [Organización Mundial de la Salud (OMS)](https://www.who.int/es), que evalúa la adecuación del peso de una persona en relación con su altura para estimar la grasa corporal.

    * **Fórmula:** $IMC = \frac{\text{peso (kg)}}{\text{altura (m)}^2}$

    El IMC nos permite clasificar el estado nutricional de una persona en categorías. La OMS ha definido la siguiente clasificación estándar del estado nutricional en adultos:

      - Bajo peso ($<18.5$)
      - Normal ($18.5-24.9$)
      - Sobrepeso ($25-29.9$)
      - Obesidad ($\ge 30$)

     * **CASOS DE USO**
        1. **El peso se mide en kilogramos
        2. **La estatura se mide en centímetros
        3. **El peso debe ser mayor a 1 kilogramo
        4. **El peso debe ser menor a 700 kilogramos
        5. **La estatura debe ser mayor a 100 centímetros
        6. **La estatura debe ser menor a 300 centímetros
        7. **Los valores deben ser números naturales
        


![Clasificación del estado nutricional de una persona.](resources/images/bmi.jpeg)

---

* **M2: Peso Corporal Ideal (PCI) o _Ideal Body Weight (IBW)_:** El PCI estima el peso teórico que se asocia con el menor riesgo de mortalidad y una mejor salud para un persona.

    **Fórmula de Lorentz (1929)**
    Es la fórmula más sencilla de aplicar manualmente ya que utiliza directamente la estatura en centímetros y no requiere conversiones a pulgadas.

        - **Hombres:** $PCI = (Estatura en cm - 100) - \frac{Estatura - 150}{4}$
        - **Mujeres:** $PCI = (Estatura en cm - 100) - \frac{Estatura - 150}{2}$

    **Nota:** Para convertir la estatura de **cm a pulgadas**, hay que dividir los centímetros entre **2.54**.

    * **CASOS DE USO**
        1. **La estatura debe introducirse en centímetros
        2. **La estatura debe ser un número mayor de 100
        3. **La estatura debe ser un número menor de 300
---

* **M5: Índice de Cintura-Cadera (ICC) o _Waist-to-Hip Ratio_ (WHR):** Es ICC la relación entre el perímetro de la cintura y el de la cadera. Se utiliza para identificar la distribución de la grasa (cuerpo tipo "manzana" o "pera") y estimar el riesgo de enfermedades cardiovasculares.
  
    * **Fórmula:** $ICC = \frac{\text{Circunferencia de cintura (cm)}}{\text{Circunferencia de cadera (cm)}}$
    * **Valores de Riesgo (OMS):**  
        - **Hombres:** $> 0.90$  
        - **Mujeres:** $> 0.85$

    Tipos de Morfología:

    1.  **Cuerpo en forma de Manzana (Androide):**
        * **Definición:** La grasa se acumula principalmente en la zona abdominal (tronco).
        * **Implicación Clínica:** Mayor riesgo de hipertensión, diabetes tipo 2 y enfermedades cardíacas debido a la cercanía de la grasa a los órganos vitales (grasa visceral).
        * **Criterio:** Se asigna si el ICC supera los límites de la OMS (>0.90 en hombres, >0.85 en mujeres).

    2.  **Cuerpo en forma de Pera (Ginoide):**
        * **Definición:** La grasa se almacena mayoritariamente en la cadera, glúteos y muslos.
        * **Implicación Clínica:** Generalmente asociada a un menor riesgo metabólico que la forma de manzana, aunque puede relacionarse con problemas articulares o varices.
        * **Criterio:** Se asigna si el ICC está dentro de los rangos normales o bajos.

    | Sexo | Rango ICC | Categoría Morfológica | Riesgo de Salud |
    | :--- | :--- | :--- | :--- |
    | **Hombre** | $\le 0.90$ | Pera (Ginoide) | Bajo / Moderado |
    | **Hombre** | $> 0.90$ | **Manzana (Androide)** | **Alto** |
    | **Mujer** | $\le 0.85$ | Pera (Ginoide) | Bajo / Moderado |
    | **Mujer** | $> 0.85$ | **Manzana (Androide)** | **Alto** |

</details>

## Plan de pruebas

Para garantizar que la calculadora sea fiable y segura, se han definido los siguientes casos de prueba divididos por categorías:

<details>
<summary><b>Pruebas de Cálculo del Índice de Masa Corporal (IMC o BMI)</b></summary>

* **Cálculo correcto:** Se comprueba que, al introducir un peso y altura normales, el resultado sea el esperado matemáticamente.
* **Protección ante datos imposibles:**
    * El sistema debe rechazar pesos menores a 1 kg o mayores a 700 kg.
    * El sistema debe rechazar alturas menores a 30 cm o mayores a 300 cm.
* **Protección ante errores de escritura:** Se verifica que no se permitan valores negativos o iguales a cero.

</details>

<details>
<summary><b>Pruebas de Clasificación del Estado de Salud basado en el IMC/BMI</b></summary>
Para cada categoría, probamos valores que están justo en el límite para asegurar que el cambio de etiqueta es exacto:  

* **Peso bajo (Underweight):** Se comprueba con valores por debajo de 18.5.
* **Peso normal (Normal weight):** Se comprueba con valores desde 18.5 hasta justo antes de 25.
* **Sobrepeso (Overweight):** Se comprueba con valores desde 25 hasta justo antes de 30.
* **Obesidad (Obesity):** Se comprueba con valores desde 30 en adelante.
* **Seguridad:** Se rechazan clasificaciones para resultados de IMC negativos o absurdamente altos (más de 150).

</details>


## Instalación y ejecución

<details>
<summary><b>Python</b></summary>

### Dependencias
- Python 3.13+
- pytest
- coverage
- pytest-cov

### Preparación del entorno
1. Clonar este repositorio: `git clone https://github.com/IngSoftAvanz/healthcalc.git`
2. Desplazarse a la carpeta del proyecto:
   `cd healthcalc/python-project-healthcalc`
3. Crear entorno virtual: `python -m venv env` (esto crea una carpeta `env` para el entorno virtual)
4. Activar el entorno virtual:
    - En Windows: `.\env\Scripts\Activate`
    - En Linux: `. env/bin/activate`
5. Instalar dependencias: `pip install -r requirements.txt`

### Ejecución
- Ejecutar la aplicación: `python main.py <número>`
- Ejecutar los tests: `pytest -v`
- Ejecutar los tests con informe de cobertura: `pytest -v --cov=factorial --cov-report=html tests/`

</details>


<details>
<summary><b>Java</b></summary>

### Dependencias
- Java JDK 18+
- Maven
- JUnit
- Jacoco
  
### Preparación del entorno
1. Clonar este repositorio: `git clone https://github.com/IngSoftAvanz/healthcalc.git`
2. Desplazarse a la carpeta del proyecto:
   `cd healthcalc/java-project-healthcalc`
3. Compilar con Maven: `mvn clean compile`


### Ejecución
- Ejecutar la aplicación: Clic en Run usando el IDE.
- Ejecutar los tests: Clic en Run Tests usando el IDE o con Maven: `mvn test`
- Ejecutar los tests con informe de cobertura (previamente configurado en pom.xml): `mvn test`

</details>