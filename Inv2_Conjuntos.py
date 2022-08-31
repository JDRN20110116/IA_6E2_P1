print("Jose David Rodriguez Navarro 20110116")
print("Tarea de investigacion 2")

c_U = set([1,2,3,4,5,6,7,8,9,10,11,12,13])                
c_V = set(["         "])                                     
c_P = set([2,4,6,8,10,12])                                 
c_I = set([1,2,3,5,7,11,13])                                   

print("\nLos elementos del conjunto universal son",c_U)
print("Los elementos del conjunto vacio son",c_V)
print("Los elementos del conjunto par son",c_P)
print("Los elementos del conjunto impar son",c_I)

cIP = c_P.union(c_I)
print("\n\nLos elementos del conjunto par en union con impar son",cIP)

cIP = c_P.intersection(c_I)
print("\n\nLos elementos del conjunto par en interseccion con impar son",cIP)

cIP = c_P.difference(c_I)
print("\n\nLos elementos del conjunto par diferentes al impar son",cIP)

gI = c_U.symmetric_difference(c_P)       
print("\n\nLa difererencia simetrica del conjunto universal y el conjunto par es:", gI)

gI = c_U.symmetric_difference(c_I)       
print("\n\nLa difererencia simetrica del cpnjunto universal y el conjunto impar es:", gI)
