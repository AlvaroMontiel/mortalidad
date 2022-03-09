class ImportarArchivo:
    def __init__(self, ruta_defunciones, ruta_poblacion):
        self.__ruta_defunciones = ruta_defunciones
        self.__ruta_poblacion = ruta_poblacion
        self.poblacion = ImportarArchivo.importar_dataset_poblacion(self)
        self.defunciones = ImportarArchivo.importar_dataset_defunciones(self)

    def importar_dataset_poblacion(self):
        import pandas as pd
        import os
        path_poblacion = os.path.abspath(self.__ruta_poblacion)

        df_poblacion = pd.read_excel(path_poblacion)

        return df_poblacion

    def importar_dataset_defunciones(self):
        import pandas as pd
        import os

        path_defunciones = os.path.abspath(self.__ruta_defunciones)

        df_defunciones = pd.read_csv(path_defunciones, sep=';', encoding='Latin',
                                     dtype={21: str, 36: str, 37: str, 38: str, 39: str,
                                            40: str, 41: str, 42: str, 43: str, 44: str,
                                            45: str, 46: str, 47: str, 48: str, 49: str,
                                            50: str, 58: str, 60: str, 64: str, 67: str,
                                            69: str, 70: str, 71: str, 73: str, 76: str,
                                            82: str, 86: str, 89: str, 90: str, 91: str,
                                            93: str, 96: str, 97: str, 98: str, 99: str,
                                            100: str})

        return df_defunciones


if __name__ == "__main__":
# Creación del objeto ImportarArchivo
    datos = ImportarArchivo("/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv",
                            "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/poblacion_corto.xlsx")

    print(datos.poblacion.shape
    print(datos.defunciones.shape)