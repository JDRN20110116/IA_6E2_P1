import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto, 4)
print(busqueda)

