enfermedades = {1: {"A00-B99":"Ciertas enfermedades infecciosas y parasitarias"},
                2: {"C00-D48": "Tumores [neoplasias]"},
                3: {"D50-D89": "Enfermedades de la sangre y de los órganos hematopoyéticos y ciertos transtornos que afectan el mecanismo de la inmunidad"},
                4: {"E00-E90": "Enfermedades endocrinas, nutricionales y metabólicas"},
                5: {"F00-F99": "Transtornos mentales y del comportamiento"},
                6: {"G00-G99": "Enfermedades del sistema nervioso"},
                7: {"H00-H59": "Enfermedades del ojo y sus anexos"},
                8: {"H60-H95": "Enfermedades del oído y de la apófisis mastoides"},
                9: {"I00-I99": "Enfermedades del sistema circulatorio"},
                10:{"J00-J99": "Enfermedades del sistema respiratorio"},
                11:{"K00-K93": "Enfermedades del sistema digestivo"},
                12:{"L00-L99": "Enfermedades de la piel y del tejido subcutáneo"},
                13:{"M00-M99": "Enfermedades del sistema osteomuscular y del tejido conjuntivo"},
                14:{"N00-N99": "Enfermedades del sistema genitourinario"},
                15:{"O00-O99": "Embarazo, parto y puerperio"},
                16:{"P00-P96": "Ciertas afecciones originadas en el período perinatal"},
                17:{"Q00-Q99": "Malformaciones congénitas, deformaciones y anomalías cromosómicas"},
                18:{"R00-R99": "Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"},
                19:{"S00-T98": "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"},
                20:{"V01-Y98": "Causas externas de morbilidad y de mortalidad"},
                21:{"Z00-Z99": "Factores que influyen en el estado de salud y contacto con los servicios de salud"},
                22:{"U00-U99": "Códigos para propósitos especiales"}}

edad = (23, 45, 4, 99, 10, 35)
edad_tipo = (1,1,1,2,1,1)

edades = list(zip(edad, edad_tipo))
print(edades)