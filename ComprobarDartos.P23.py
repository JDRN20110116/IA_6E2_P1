colores = input('Introduce un color:\n')
tupla_colores = ('turquesa', 'verde', 'naranja', 'morado')

if colores in tupla_colores[0]:
	print('El color turquesa está admitido')

elif colores in tupla_colores[1]:
	print('El color verde está admitido')

elif colores in tupla_colores[2]:
	print('El color naranja está admitido')

elif colores in tupla_colores[3]:
	print('El color morado está admitido')

else:
	print('Color no admitido')
