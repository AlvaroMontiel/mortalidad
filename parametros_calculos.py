from importar_archivo import ImportarArchivo

class ParametrosCalculos(ImportarArchivo):
    '''
    Esta clase importa el dataset correspondiente a poblacion y defunciones y los procesa de acuerdo a los parámetros
    entregados por el usuario
    El método importar data set es heredado de la clase ImportarArchivo.py y sirve para crear los objetos que contienen
    los dataframes de poblacion y de defunciones
    '''
    def __init__(self, extension, ruta, periodo, sexo=None, region=None, comuna=None, edad=False):
        super().__init__(extension, ruta)
        self.periodo = periodo
        self.sexo = sexo
        self.region = region
        self.comuna = comuna
        self.edad = edad

    def __importar_dataset(self):
        super().__importar_dataset()

    def aplicar_periodo_defuncion(self):
        super().__importar_dataset()



if __name__ == "__main__":
    poblacion = ParametrosCalculos("xlsx",
                                "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/poblacion_corto.xlsx",
                                   "2014-2018")
    defunciones = ParametrosCalculos("csv",
                                  "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv",
                                     "2014-2018")
    print(poblacion.dataframe.shape)
    print(defunciones.dataframe.shape)

