from importar_archivo import ImportarArchivo
from agrupacion_edad import AgrupacionEdad

class ParametrosCalculos(ImportarArchivo):
    '''
    Esta clase importa el dataset correspondiente a poblacion y defunciones y los procesa de acuerdo a los parámetros
    entregados por el usuario
    El método importar data set es heredado de la clase ImportarArchivo.py y sirve para crear los objetos que contienen
    los dataframes de poblacion y de defunciones
    '''
    def __init__(self, ruta_defunciones, ruta_poblacion, periodo, enfermedad,
                 edad=0, region=None, comuna=None):
        super().__init__(ruta_defunciones, ruta_poblacion)
        self.periodo = periodo
        self.enfermedad = enfermedad
        self.edad = edad
        self.region = region
        self.comuna = comuna
        self.datos = ParametrosCalculos.importar_dataframe(self)
        self.poblacion_filtrada = ParametrosCalculos.filtrar_poblacion(self)
        self.defunciones_filtradas = ParametrosCalculos.filtrar_defunciones(self)

    # la función crea un objeto Importar Archivo que contiene los dataframe defunciones y población
    def importar_dataframe(self):
        datos_ = ImportarArchivo(self.ruta_defunciones, self.ruta_poblacion)

        return datos_

    def filtrar_periodo_defunciones(self):
        # Filtra el dataframe de defunciones y devuelve el dataframe por el periodo solicitado
        periodo = self.periodo.split("-")
        per_inicial = int("".join(periodo[0]))
        per_final = int("".join(periodo[1]))
        b = per_final - per_inicial
        x = []
        if b == 0:
            x.append(per_inicial)
        elif b >= 1:
            b += 1
            for i in range(b):
                x.append(per_inicial)
                per_inicial += 1
        df = self.datos.defunciones[
            self.datos.defunciones['ANO_DEF'].isin(x)]  # Eliminé el .copy() para ahorrar memoria

        return df

    def filtrar_enfermedad_defunciones(self):
        # aplica el filtro por periodo, NO OLVIDAR QUE ES UNA COPIA ALOJADA EN EL MISMO SITIO DE MEMORIA
        df = self.filtrar_periodo_defunciones()
        # ahora debo filtrar por la enfermedad solicitada por el usuario
        if self.enfermedad == 0:
            df = df
        elif self.enfermedad == 1:
            df = df.query('CAPITULO_DIAG1 == "A00-B99"')
        elif self.enfermedad == 2:
            df = df.query('CAPITULO_DIAG1 == "C00-D48"')
        elif self.enfermedad == 3:
            df = df.query('CAPITULO_DIAG1 == "D50-D89"')
        elif self.enfermedad == 4:
            df = df.query('CAPITULO_DIAG1 == "E00-E90"')
        elif self.enfermedad == 5:
            df = df.query('CAPITULO_DIAG1 == "F00-F99"')
        elif self.enfermedad == 6:
            df = df.query('CAPITULO_DIAG1 == "G00-G99"')
        elif self.enfermedad == 7:
            df = df.query('CAPITULO_DIAG1 == "H00-H59"')
        elif self.enfermedad == 8:
            df = df.query('CAPITULO_DIAG1 == "H60-H95"')
        elif self.enfermedad == 9:
            df = df.query('CAPITULO_DIAG1 == "I00-I99"')
        elif self.enfermedad == 10:
            df = df.query('CAPITULO_DIAG1 == "J00-J99"')
        elif self.enfermedad == 11:
            df = df.query('CAPITULO_DIAG1 == "K00-K93"')
        elif self.enfermedad == 12:
            df = df.query('CAPITULO_DIAG1 == "L00-L99"')
        elif self.enfermedad == 13:
            df = df.query('CAPITULO_DIAG1 == "M00-M99"')
        elif self.enfermedad == 14:
            df = df.query('CAPITULO_DIAG1 == "N00-N99"')
        elif self.enfermedad == 15:
            df = df.query('CAPITULO_DIAG1 == "O00-O99"')
        elif self.enfermedad == 16:
            df = df.query('CAPITULO_DIAG1 == "P00-P96"')
        elif self.enfermedad == 17:
            df = df.query('CAPITULO_DIAG1 == "Q00-Q99"')
        elif self.enfermedad == 18:
            df = df.query('CAPITULO_DIAG1 == "R00-R99"')
        elif self.enfermedad == 19:
            df = df.query('CAPITULO_DIAG1 == "S00-T98"')
        elif self.enfermedad == 20:
            df = df.query('CAPITULO_DIAG1 == "V01-Y98"')
        elif self.enfermedad == 21:
            df = df.query('CAPITULO_DIAG1 == "Z00-Z99"')
        elif self.enfermedad == 22:
            df = df.query('CAPITULO_DIAG1 == "U00-U99"')

        return df

    def agrupar_edad_defunciones(self):
        df = self.filtrar_enfermedad_defunciones()
        if self.edad == 0:
            df = df
        elif self.edad >= 1:
            edad = df['EDAD_CANT'].values.tolist()
            edad_tipo = df['EDAD_TIPO'].values.tolist()
            edades = list(zip(edad, edad_tipo))
            edad_categoria = list()
            if self.edad == 1:
                for tupla in edades:
                    if tupla[1] == 1:
                        if tupla[0] >= 1 and tupla[0] <= 4:
                            edad_categoria.append(1)
                        elif tupla[0] >= 5 and tupla[0] <= 9:
                            edad_categoria.append(2)
                        elif tupla[0] >= 10 and tupla[0] <= 14:
                            edad_categoria.append(3)
                        elif tupla[0] >= 15 and tupla[0] <= 19:
                            edad_categoria.append(4)
                        elif tupla[0] >= 20 and tupla[0] <= 24:
                            edad_categoria.append(5)
                        elif tupla[0] >= 25 and tupla[0] <= 29:
                            edad_categoria.append(6)
                        elif tupla[0] >= 30 and tupla[0] <= 34:
                            edad_categoria.append(7)
                        elif tupla[0] >= 35 and tupla[0] <= 39:
                            edad_categoria.append(8)
                        elif tupla[0] >= 40 and tupla[0] <= 44:
                            edad_categoria.append(9)
                        elif tupla[0] >= 45 and tupla[0] <= 49:
                            edad_categoria.append(10)
                        elif tupla[0] >= 50 and tupla[0] <= 54:
                            edad_categoria.append(11)
                        elif tupla[0] >= 55 and tupla[0] <= 59:
                            edad_categoria.append(12)
                        elif tupla[0] >= 60 and tupla[0] <= 64:
                            edad_categoria.append(13)
                        elif tupla[0] >= 65 and tupla[0] <= 69:
                            edad_categoria.append(14)
                        elif tupla[0] >= 70 and tupla[0] <= 74:
                            edad_categoria.append(15)
                        elif tupla[0] >= 75 and tupla[0] <= 79:
                            edad_categoria.append(16)
                        elif tupla[0] >= 80:
                            edad_categoria.append(17)
                    elif tupla[1] >= 2:
                        edad_categoria.append(1)
                df['EDAD_CAT'] = edad_categoria
            elif self.edad == 2:
                # 1: 0-17, 2: 18-59, 3: 60 y mas
                for tupla in edades:
                    if tupla[1] == 1:
                        if tupla[0] <= 17:
                            edad_categoria.append(1)
                        elif tupla[0] >= 18 and tupla[0] <= 59:
                            edad_categoria.append(2)
                        elif tupla[0] >= 60:
                            edad_categoria.append(3)
                    elif tupla[1] >= 2:
                        edad_categoria.append(1)
                df['EDAD_CAT'] = edad_categoria
            elif self.edad == 3:
                pass

        return df

    def filtrar_geografia_defunciones(self):
        x = list()
        y = list()
        x.append(self.region)
        y.append(self.comuna)
        df = self.agrupar_edad_defunciones()
        if self.region == None and self.comuna == None:
            df = df
        elif self.region != None and self.comuna == None:
            df = df[df['REG_RES'].isin(x)]
        elif self.region == None and self.comuna != None:
            df = df[df['COMUNA'].isin(y)]

        return df

    def filtrar_defunciones(self):
        df = self.filtrar_geografia_defunciones()

        return df

    def filtrar_geografia_poblaciones(self):
        if self.region == None and self.comuna == None:
            df_ = self.datos.poblacion
        elif self.region != None and self.comuna == None:
            df_ = self.datos.poblacion[(self.datos.poblacion.Region == self.region)]
        elif self.region == None and self.comuna != None:
            df_ = self.datos.poblacion[self.datos.poblacion.Comuna == self.comuna ]
        return df_

    def agrupar_edad_poblaciones(self):
        df_ = self.filtrar_geografia_poblaciones()
        if self.edad == 0:
            df_ = df_
        elif self.edad >= 1:
            edad_categoria = list()
            lista_edad = df_['Edad'].values.tolist()
            if self.edad == 1:
                for edad in lista_edad:
                    if edad >= 0 and edad <= 4:
                        edad_categoria.append(1)
                    elif edad >= 5 and edad <= 9:
                        edad_categoria.append(2)
                    elif edad >= 10 and edad <= 14:
                        edad_categoria.append(3)
                    elif edad >= 15 and edad <= 19:
                        edad_categoria.append(4)
                    elif edad >= 20 and edad <= 24:
                        edad_categoria.append(5)
                    elif edad >= 25 and edad <= 29:
                        edad_categoria.append(6)
                    elif edad >= 30 and edad <= 34:
                        edad_categoria.append(7)
                    elif edad >= 35 and edad <= 39:
                        edad_categoria.append(8)
                    elif edad >= 40 and edad <= 44:
                        edad_categoria.append(9)
                    elif edad >= 45 and edad <= 49:
                        edad_categoria.append(10)
                    elif edad >= 50 and edad <= 54:
                        edad_categoria.append(11)
                    elif edad >= 55 and edad <= 59:
                        edad_categoria.append(12)
                    elif edad >= 60 and edad <= 64:
                        edad_categoria.append(13)
                    elif edad >= 65 and edad <= 69:
                        edad_categoria.append(14)
                    elif edad >= 70 and edad <= 74:
                        edad_categoria.append(15)
                    elif edad >= 75 and edad <= 79:
                        edad_categoria.append(16)
                    elif edad >= 80:
                        edad_categoria.append(17)
                df_['EDAD_CAT'] = edad_categoria
            elif self.edad == 2:
                # 1: 0-17, 2: 18-59, 3: 60 y mas
                for edad in lista_edad:
                    if edad >= 0 and edad <= 17:
                        edad_categoria.append(1)
                    elif edad >= 18 and edad <= 59:
                        edad_categoria.append(2)
                    elif edad >= 60:
                        edad_categoria.append(3)
                df_['EDAD_CAT'] = edad_categoria
            elif self.edad == 3:
                pass
        return df_

    def filtrar_periodo_poblaciones(self):
        df_ = self.agrupar_edad_poblaciones()
        periodo_poblacion = self.periodo.split("-")
        per_inicial = int("".join(periodo_poblacion[0]))
        per_final = int("".join(periodo_poblacion[1]))
        tipo_per = (per_final - per_inicial) + 1
        nom_columna = df_.columns.values.tolist()

        if tipo_per % 2 > 0:
            a = 0
            b = 0
            for i in range(0, tipo_per):
                a += 1
                b = b + a
            ano_poblacion = int((per_inicial + (b / a)) - 1)
            poblacion = "Poblacion" + " " + str(ano_poblacion)
            for i in range(8, len(nom_columna)):
                if nom_columna[i] == poblacion:
                    pass
                elif nom_columna[i] != poblacion:
                    df_ = df_.drop(columns=[nom_columna[i]])
        elif tipo_per % 2 == 0:
            # Crea dos años
            if per_final - per_inicial == 1:  # bienio
                poblacion_1 = "Poblacion" + " " + str(per_inicial)
                poblacion_2 = "Poblacion" + " " + str(per_final)
                for i in range(8, len(nom_columna)):
                    if nom_columna[i] == poblacion_1 or nom_columna == poblacion_2:
                        pass
                    elif nom_columna[i] != poblacion_1 and nom_columna[i] != poblacion_2:
                        df_ = df_.drop(columns=[nom_columna[i]])
            elif per_final - per_inicial > 1: # cuatrienio y más
                a = 0
                b = 0
                for i in range(0, tipo_per):
                    a += 1
                    b = b + a
                    poblacion_1 = "Poblacion" + " " + str(int(per_inicial + ((b / a) - 0.5) - 1))
                    poblacion_2 = "Poblacion" + " " + str(int(per_inicial + ((b / a) + 0.5) - 1))

                for i in range(8, len(nom_columna)):
                    if nom_columna[i] == poblacion_1 or nom_columna == poblacion_2:
                        pass
                    elif nom_columna[i] != poblacion_1 and nom_columna[i] != poblacion_2:
                        df_ = df_.drop(columns=[nom_columna[i]])

        return df_


    def filtrar_poblacion(self):
        print("Se está ejecutando el módulo Parámetros Cálculos")
        df_ = self.filtrar_periodo_poblaciones()
        return df_




if __name__ == "__main__":
    datos = ParametrosCalculos("/Users/alvaro/Documents/Data_Science/Software_mortalidad/mortalidad/datasets/DEF_2010_2018.csv",
                               "/Users/alvaro/Documents/Data_Science/Software_mortalidad/mortalidad/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx",
                               "2014-2014", 2, region=2, edad = 2)

    print(datos.poblacion_filtrada.columns.values.tolist())


