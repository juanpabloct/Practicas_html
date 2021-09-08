from math import nan
from numpy import NaN, tan
import pandas as pd
import random
"""
datos = {
    'temperaturas': [22,24,17,19,22,21,23,25,21,23,27,19],
    'humedades': [80,70,75,74,90,74,75,86,74,78,79,81],
    'velocidad_del_viento': [random.randint(5, 50) for i in range(12)]
}
df_clima=pd.DataFrame(datos, index=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
df_clima.columns.name='Meses'

# Practica#
estudiantes = [{"nombre": "Andrea", "apellido": "Rodriguez", "documento": "555437", "sexo": "F"}, {"nombre": "Jackie", "apellido": "Chan", "documento": "4242332", "sexo": "M", 'edad':12}, {"nombre": "Juan ", "apellido": "Castro", "documento": "82736", "sexo": "M"}, {"nombre": "Zara", "apellido": "Santana", "documento": "6789", "sexo": "F", 'edad':23}, {
    'nombre': 'Andres',
    'apellido': 'Rodriguez',
    'documento': '1111',
    'sexo':'F',
    'edad':20
}]

Table_estudiantes=pd.DataFrame(estudiantes)
df_clima['Energia Termica']=(df_clima.temperaturas*df_clima.velocidad_del_viento-30)
df_clima['temperaturas']=[34, 19, 10, 12, 20, 16, 26, 34, 36, 40, 42, 15]
df_clima['temperaturas']=[12, 33, 45, 4, 23, 23,12, 32, 12, 21, 19, 18]
lista_edad=list(Table_estudiantes.edad)
edades=pd.Series(lista_edad)
Information_edad=edades.value_counts(dropna=False)
#print(Information_edad)
#print('________________________________________________________')
humedades=pd.Series([90, 20, 60, 56, 98, 23, 

 23, 32, 54, 23, 65, 98], index=['enero', 'febrero', 'Marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'])
#print(humedades.value_counts(bins=4))
humedades['mayo']=46
#print(humedades[1: 11])
#print(humedades[['enero', 'abril']])
#print(humedades.loc[['enero', 'abril']])
print(Table_estudiantes.sort_values(by=['apellido', 'nombre']))
"""

dicccionario_de_estudiantes=[{
    'Nombre':'Juana',
    'Curso':'Noveno',
    'Edad':20
},
{
    'Nombre':'Andrea',
    'Curso':'Once',
    'Edad':17
}, {
    'Nombre':'Carlos',
    'Curso':'Decimo',
    'Edad':15
}
]

table_estudiantes=pd.DataFrame(dicccionario_de_estudiantes)
print(table_estudiantes)