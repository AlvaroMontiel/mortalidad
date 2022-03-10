class AgrupacionEdad:
    def __init__(self):
        pass

    def agrupar_edad(self):
        edad = 4
        while edad != 0 and edad != 1 and edad != 2 and edad != 3:
            edad = int(input("Ingresar el código de la desagregación por edad que desea analizar \n"
                         "\n"
                         "0 --> Sin agrupación por edad. \n"
                         "1 --> Agrupar por quinquenio de edad (17 grupos). \n"
                         "2 --> 0 a 15 años, 16 a 30 años, 31 a 60 años, 60 y más años. \n"
                         "3 --> Agrupación definida por el usuario. \n"
                         "\n"
                         "Digite 0, 1, 2 o 3 -->" 
                         "\n"))
            if edad == 0:
                print("Ha seleccionado el análisis sin desagregar por edad")
            elif edad == 1:
                print("Ha seleccionado 1")
            elif edad == 2:
                print("Ha seleccionado 2")
            elif edad == 3:
                print("Ha seleccionado 3")
            else:
                print(f"Ha seleccionado {edad}, debe digitar 1, 2 o 3")

        return edad

if __name__ == "__main__":
    grupo_edad = AgrupacionEdad()
    grupo_edad.agrupar_edad()