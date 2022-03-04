from codigo_main import formato_tabla_tabular as tab

def formato_tabla(datos1, datos2, tabular):
    lista_maxima = list()
    tabular3 = ["C00-C14", "C15", "C16", "C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97", "C18-C21", "C22", "C25", "C32", "C33-C34", "C43", "C50", "C53", "C54-C55", "C56", "C61", "C67", "C70-C72", "C82-C85", "C90", "C91-C95", "D00-D48"]
    tabular4 = ["C00-C14", "C15", "C16", "C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97", "C18-C21", "C22", "C25", "C32", "C33-C34", "C43", "C50", "C53", "C54-C55", "C56", "C61", "C67", "C70-C72", "C82-C85", "C90", "C91-C95"]
    tabular5 = ["C00-C14", "C15-C26", "C30-C39", "C40-C41", "C43-C44", "C45-C49", "C50", "C51-C58", "C60-C63", "C64-C68", "C69-C72", "C73-C75", "C76-C80", "C81-C96", "D10-D36", "D37-D48"]

    if tabular == 5:
        for i in tabular5:
            if i == "C00-C14":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                # for key, value in datos1.items():
                #     lista2 = list()
                #     lista2.append(key)
                #     lista2.append(i)
                #     if len(value) == 0:
                #         lista2.append(0)
                #         lista2.append(0)
                #     elif len(value) == 1:
                #         for elemento in value:
                #             if elemento[0] == i:
                #                 lista2.append(elemento[1])
                #                 valor2 = datos2.get(key)
                #                 for valor in valor2:
                #                     lista2.append(valor[1])
                #             elif elemento[0] != i:
                #                 lista2.append(0)
                #                 lista2.append(0)
                #     elif len(value) >1:
                #         contador = 0
                #         for tupla in value:
                #             if tupla[0] == i:
                #                 contador += 1
                #             elif tupla[0] != i:
                #                 pass
                #         if contador == 0:
                #             lista2.append(0)
                #             lista2.append(0)
                #         elif contador > 0:
                #             for tupla in value:
                #                 if tupla[0] == i:
                #                     lista2.append(tupla[1])
                #                     valor2 = list()
                #                     valor2 = datos2.get(key)
                #                     for valor in valor2:
                #                         if valor[0] == i:
                #                             lista2.append(valor[1])
                #     lista1.append(lista2)
                lista_maxima.append(lista1)
            elif i == "C15-C26":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C30-C39":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C40-C41":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C43-C44":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C45-C49":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C50":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C51-C58":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C60-C63":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C64-C68":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C69-C72":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C73-C75":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C76-C80":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C81-C96":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "D10-D36":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "D37-D48":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
    elif tabular == 4:
        for i in tabular4:
            if i == "C00-C14":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C15":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C16":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C18-C21":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C22":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C25":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C32":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C33-C34":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C43":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C50":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C53":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C54-C55":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C56":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C61":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C67":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C70-C72":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C82-C85":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C90":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C91-C95":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)

    elif tabular == 3:
        for i in tabular3:
            if i == "C00-C14":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C15":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C16":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C18-C21":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C22":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C25":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C32":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C33-C34":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C43":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C50":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C53":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C54-C55":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C56":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C61":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C67":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C70-C72":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C82-C85":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C90":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "C91-C95":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
            elif i == "D00-D48":
                lista1 = tab.formato_tabla_tabular3(datos1, datos2, i)
                lista_maxima.append(lista1)
    return lista_maxima
# datos1 = {1: [], 2: [(38.98635477582847, 'C91-C95')], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [(48.07692307692308, 'C53')], 10: [(53.763440860215056, 'C18-C21'), (53.763440860215056, 'C53'), (53.763440860215056, 'D00-D48')], 11: [(53.61930294906167, 'D00-D48')], 12: [(57.47126436781609, 'C18-C21'), (57.47126436781609, 'C33-C34')], 13: [(65.14657980456026, 'C15'), (130.29315960912052, 'C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97'), (65.14657980456026, 'C25'), (65.14657980456026, 'C33-C34'), (65.14657980456026, 'C70-C72')], 14: [(102.04081632653062, 'C18-C21'), (102.04081632653062, 'C25'), (102.04081632653062, 'C33-C34'), (102.04081632653062, 'C50'), (102.04081632653062, 'C54-C55'), (102.04081632653062, 'C91-C95')], 15: [(136.0544217687075, 'C50')], 16: [(212.76595744680853, 'C16'), (638.2978723404254, 'C67'), (212.76595744680853, 'C91-C95'), (212.76595744680853, 'D00-D48')], 17: [(106.38297872340426, 'C16'), (212.76595744680853, 'C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97'), (212.76595744680853, 'C18-C21'), (106.38297872340426, 'C50'), (106.38297872340426, 'C67'), (106.38297872340426, 'C91-C95'), (319.1489361702127, 'D00-D48')]}
# datos2 = {1: [], 2: [('C91-C95', 1)], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [('C53', 1)], 10: [('C18-C21', 1), ('C53', 1), ('D00-D48', 1)], 11: [('D00-D48', 1)], 12: [('C18-C21', 1), ('C33-C34', 1)], 13: [('C15', 1), ('C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97', 2), ('C25', 1), ('C33-C34', 1), ('C70-C72', 1)], 14: [('C18-C21', 1), ('C25', 1), ('C33-C34', 1), ('C50', 1), ('C54-C55', 1), ('C91-C95', 1)], 15: [('C50', 1)], 16: [('C16', 1), ('C67', 3), ('C91-C95', 1), ('D00-D48', 1)], 17: [('C16', 1), ('C17, C23-C24, C26-C31, C37-C41, C44-C49, C51-C52, C57-C60, C62-C66, C68-C69, C73-C81, C88,C96-C97', 2), ('C18-C21', 2), ('C50', 1), ('C67', 1), ('C91-C95', 1), ('D00-D48', 3)]}
# a = formato_tabla(datos1,datos2,5)
# #print(a)
# for lista in a:
#     print("==="*50)
#     print(lista)
#     print("==="*50)