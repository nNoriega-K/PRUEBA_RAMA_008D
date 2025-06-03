alumnos = {}
num_alumnos =  int(input("Ingrese el número de alumnos del curso "))
contador_alumnos = 0
while  contador_alumnos < num_alumnos:
    nom_alumno = input("Ingrese el nombre del alumno")
    if nom_alumno in alumnos:
       print("Error:  Alumno ya existe")
    else:
        loop_ok =  True
        lista_notas = []
        while  loop_ok:
            nota = float(input("Ingrese la nota del alumno "))
            if nota > 0:
                lista_notas.append(nota)
            else:
                 loop_ok =  False
        alumnos[nom_alumno] = lista_notas
        contador_alumnos = contador_alumnos + 1
for  nom_alumn in alumnos:
    cant_notas = 0
    suma_notas = 0
    for nota_alumn in alumnos[nom_alumn]:
        cant_notas = cant_notas + 1
        suma_notas = suma_notas + nota_alumn
    promedio = round(suma_notas / cant_notas,1)
    print(f"El promedio de notas del alumno {nom_alumn} es  {promedio}")