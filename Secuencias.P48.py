import re
texto = "Se acerca el invierno."
buscar = re.findall("vierno.$", texto)
if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")
