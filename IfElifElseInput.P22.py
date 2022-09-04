edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad == 18 and edad <= 45:
	print('Eres un adulto joven, adelante.')
elif edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
	print('Se supone que no debrias de seguir vivo.')
else:
	print('Edad no válida.')