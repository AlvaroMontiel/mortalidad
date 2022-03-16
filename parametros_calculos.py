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
        self.poblacion_filtrada = None
        self.defunciones_filtradas = ParametrosCalculos.agrupar_edad_defunciones(self)

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
        df = self.agrupar_edad_defunciones()
        if self.region == None and self.comuna == None:
            df = df
        elif self.region != None and self.comuna == None:
            df = df[df['REG_RES'].isin(self.region)]
        elif self.region == None and self.comuna != None:
            df = df[df['COMUNA'].isin(self.comuna)]

        return df

    def agrupar_edad_poblacion(self):
        if self.edad == 0:
            pass
        elif self.edad >= 1:
            pass


    def filtrar_poblacion(self):
        pass


    def filtrar_periodo_poblacion(self):
        pass

    def filtrar_defunciones(self):
        pass
        # if self.edad == 0:
        #     pass
        # elif self.edad >= 1:
        #     pass

        # return df



if __name__ == "__main__":

    for i in range(1,3):
        datos = ParametrosCalculos("/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv",
                                   "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/poblacion_corto.xlsx",
                                   "2014-2018", i, 2, region=2)

        print(datos.defunciones_filtradas[['EDAD_CANT','EDAD_CAT']])

