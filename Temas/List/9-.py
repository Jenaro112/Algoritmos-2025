""" 
9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un algoritmo que permita realizar la siguientes actividades:
-   a. mostrar los alumnos ordenados alfabéticamente por apellido;
-   b. indicar los alumnos que no desaprobaron ningún parcial;
-   c. determinar los alumnos que tienen promedio mayor a 8,89;
-   d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
-   e. mostrar el promedio de cada uno de los alumnos;
-   f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
-   g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
-   h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
-   i. mostrar todos los alumnos que rindieron en el año 2020;
"""
from list_ import List

class Alumno:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.legajo = ""
        self.examenes = List()

    def __str__(self):
        return (f"- Nombre: {self.nombre}\n"
                f"- Apellido: {self.apellido}\n"
                f"- Legajo: {self.legajo}\n"
                f"- Exámenes:\n" + "\n".join(str(examen) for examen in self.examenes))


class Examen:
    def __init__(self):
        self.materia = ""
        self.nota = 0
        self.fecha = ""

    def __str__(self):
        return (f"- Materia: {self.materia}"
                f"- Nota: {self.nota}"
                f"- Fecha: {self.fecha}")


# Punto A
def Punto_a(lista: List) -> List:
    return List(sorted(lista, key=lambda a: a.apellido))

# Punto B
def Punto_b(lista: List) -> List:
    return List([alumno for alumno in lista if all(examen.nota >= 6 for examen in alumno.examenes)])

# Punto C
def Punto_c(lista: List) -> List:
    return List([alumno for alumno in lista if alumno.examenes and 
                sum(ex.nota for ex in alumno.examenes) / len(alumno.examenes) > 8.89])

# Punto D
def Punto_d(lista: List) -> List:
    return List([alumno for alumno in lista if alumno.apellido.startswith("L")])

# Punto E
def Punto_e(lista: List) -> List:
    return List([(alumno, sum(ex.nota for ex in alumno.examenes) / len(alumno.examenes))
                for alumno in lista if alumno.examenes])

# Punto F
def Punto_f(lista: List) -> List:
    return List([alumno for alumno in lista if any(ex.materia == "Algoritmos y estructuras de datos"
                                                    for ex in alumno.examenes)])

# Punto G
def Punto_g(lista: List, legajo: str) -> float:
    for alumno in lista:
        if alumno.legajo == legajo:
            total = len(alumno.examenes)
            aprobados = sum(1 for ex in alumno.examenes if ex.nota >= 6)
            return (aprobados / total) * 100 if total > 0 else 0.0
    return None  # No encontrado

# Punto H
def Punto_h(lista: List) -> dict:
    aprobados = 0
    desaprobados = 0
    for alumno in lista:
        for examen in alumno.examenes:
            if examen.materia == "Base de datos":
                if examen.nota >= 6:
                    aprobados += 1
                else:
                    desaprobados += 1
    return {"Aprobados": aprobados, "Desaprobados": desaprobados}

# Punto I
def Punto_i(lista: List) -> List:
    return List([alumno for alumno in lista if any(ex.fecha.startswith("2020") for ex in alumno.examenes)])


# Programa principal
if __name__ == "__main__":
    lista_alumnos = List()

    # Carga de ejemplo
    alumno1 = Alumno()
    alumno1.nombre = "Juan"
    alumno1.apellido = "Perez"
    alumno1.legajo = "12345"

    examen1 = Examen()
    examen1.materia = "Algoritmos y estructuras de datos"
    examen1.nota = 9
    examen1.fecha = "2020-05-20"

    examen2 = Examen()
    examen2.materia = "Base de datos"
    examen2.nota = 7
    examen2.fecha = "2020-06-15"

    alumno1.examenes.append(examen1)
    alumno1.examenes.append(examen2)

    lista_alumnos.append(alumno1)

    print("="*50)
    print("A) Alumnos ordenados por apellido:")
    for a in Punto_a(lista_alumnos):
        print(a)

    print("="*50)
    print("B) Alumnos que NO desaprobaron ningún parcial:")
    for a in Punto_b(lista_alumnos):
        print(a)

    print("="*50)
    print("C) Alumnos con promedio mayor a 8.89:")
    for a in Punto_c(lista_alumnos):
        print(a)

    print("="*50)
    print("D) Alumnos cuyos apellidos comienzan con 'L':")
    for a in Punto_d(lista_alumnos):
        print(a)

    print("="*50)
    print("E) Promedio de cada alumno:")
    for alumno, promedio in Punto_e(lista_alumnos):
        print(f"{alumno.nombre} {alumno.apellido} (Legajo {alumno.legajo}): {promedio:.2f}")

    print("="*50)
    print("F) Alumnos que rindieron 'Algoritmos y estructuras de datos':")
    for a in Punto_f(lista_alumnos):
        print(a)

    print("="*50)
    legajo_usuario = "12345"
    porcentaje = Punto_g(lista_alumnos, legajo_usuario)
    print(f"G) Porcentaje de parciales aprobados del legajo {legajo_usuario}:")
    if porcentaje is not None:
        print(f"{porcentaje:.2f}%")
    else:
        print("No se encontró el alumno con ese legajo.")

    print("="*50)
    print("H) Parciales de 'Base de datos':")
    resultado_bd = Punto_h(lista_alumnos)
    print(f"Aprobados: {resultado_bd['Aprobados']}")
    print(f"Desaprobados: {resultado_bd['Desaprobados']}")

    print("="*50)
    print("I) Alumnos que rindieron en el año 2020:")
    for a in Punto_i(lista_alumnos):
        print(a)
    print("="*50)
