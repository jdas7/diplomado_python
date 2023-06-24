import os
os.system("clear")

grupo_a= set(['Wilson', 'Hugo', 'Pipe', 'Ivan'])
grupo_b= {'Wilson', 'Juan', 'Pipe', 'Antonio'}
grupo_c= {'Wilson', 'Antonio', 'Hugo', 'Natalia'}

print(grupo_a)
print(grupo_b)
print(grupo_c)

estudiantes = grupo_a.union(grupo_b).union(grupo_c)
estudiantes_2 = grupo_a.union(grupo_b)
estudiantes_3 = grupo_a.intersection(grupo_b).intersection(grupo_c)
print(estudiantes)
print(estudiantes_2)
print(estudiantes_3)