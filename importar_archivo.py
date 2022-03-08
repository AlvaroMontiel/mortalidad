class ImportarArchivo:
    def __init__(self, extension, ruta):
        self.__extension = extension
        self.__ruta = ruta
        self.dataframe = self.__importar_dataset()

    def __importar_dataset(self):
        import pandas as pd
        import os
        path = os.path.abspath(self.__ruta)

        if self.__extension == "xlsx":
            df = pd.read_excel(path)
        elif self.__extension == "csv":
            df = pd.read_csv(path, sep=';', encoding='Latin',
                             dtype={21: str, 36: str, 37: str, 38: str, 39: str,
                                    40: str, 41: str, 42: str, 43: str, 44: str,
                                    45: str, 46: str, 47: str, 48: str, 49: str,
                                    50: str, 58: str, 60: str, 64: str, 67: str,
                                    69: str, 70: str, 71: str, 73: str, 76: str,
                                    82: str, 86: str, 89: str, 90: str, 91: str,
                                    93: str, 96: str, 97: str, 98: str, 99: str,
                                    100: str})
        else:
            print("El archivo a importar debe tener extensión xlsx o csv")

        return df


if __name__ == "__main__":
    poblacion = ImportarArchivo("xlsx", "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/estimaciones-y-proyecciones-2002-2035-comunas.xlsx")
    defunciones = ImportarArchivo("csv", "/Users/alvaro/Documents/Data_Science/Software_mortalidad/datasets/DEF_2010_2018.csv")
    print(poblacion.dataframe.shape)
    print(defunciones.dataframe.shape)
