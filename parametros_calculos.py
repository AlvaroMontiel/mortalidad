from importar_archivo import ImportarArchivo

class ParametrosCalculos(ImportarArchivo):
    '''
    Esta clase importa el dataset correspondiente a poblacion y defunciones y los procesa de acuerdo a los parámetros
    entregados por el usuario
    El método importar data set es heredado de la clase ImportarArchivo.py y sirve para crear los objetos que contienen
    los dataframes de poblacion y de defunciones
    '''
    def __init__(self, extension, ruta, periodo, enfermedad, categoria_enfermedad, sexo=None, region=None, comuna=None, edad=False):
        super().__init__(extension, ruta)
        self.periodo = periodo
        self.enfermedad = enfermedad
        self.categoria_enfermedad = categoria_enfermedad
        self.sexo = sexo
        self.region = region
        self.comuna = comuna
        self.edad = edad


    def filtrar_dataframe(self):
        defunciones = ImportarArchivo("csv", self.ruta)
        poblacion = ImportarArchivo("xlsx", self.ruta)
        if self.extension == "csv": #dataset de mortalidad
            pass
        elif self.extension == "xlsx": #dataset de poblacion
            pass

        if self.sexo == None or self.region == None or self.comuna == None or self.edad == False:
            return print(self.dataframe.shape)


    def separa_edad(self):
        pass



if __name__ == "__main__":
    poblacion = ParametrosCalculos("xlsx",
                                "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/poblacion_corto.xlsx",
                                   "2014-2018", "cancer", 1)
    print(poblacion.importar_dataset().shape)
#    defunciones = ParametrosCalculos("csv",
#                                  "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv",
#                                     "2014-2018")
#
#    print(defunciones.dataframe.shape)
