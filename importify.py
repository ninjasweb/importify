from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 
import pandas as pd

#Importamos el archivo xls como 'only read' (Sólo lectura)
file = r'avanti.xls'
#Leemos el archivo Xls
df = pd.read_excel(file)

#Remove messy data
#df = df[df['full_name'] != 'n/a']

#Seleccionamos el nombre de la columna
nombres = df['full_name']

#Importamos el XlsxWriter
import xlsxwriter

# Creamos el Workbook
workbook = xlsxwriter.Workbook('importify_file.xlsx')
# Creamos el Worksheet
worksheet = workbook.add_worksheet()

#Agregar el Formato Negrita o Bold
bold = workbook.add_format({'bold':1})

# Empezar desde la primer celda.
row = 0
col = 0

#Inicializamos la variable en 0
i=0

while i < len(nombres):	
	#Captamos el primer Nombre [0]
	primerNombre = nombres[i].partition(' ')[0]

	#Captamos el Apellido [2]
	apellidos = nombres[i].partition(' ')[2]

	#Imprimimos el nombre y los apellidos para comprobar
	#print(primerNombre, apellidos)
	#Agregamos una etiqueta
	worksheet.write('A1', 'Nombre', bold)
	worksheet.write('B1', 'Apellidos', bold)
	worksheet.write(row+1, col, primerNombre)
	worksheet.write(row+1, col +1 , apellidos)
	row += 1
	i = i + 1

	#for nombre in (primerNombre):
	#	worksheet.write(row, col, nombre)
	#	worksheet.write(row, col +1 , apellidos)
	#	row += 1

workbook.close()