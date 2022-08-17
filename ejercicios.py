def hola():
  print("Ejercicio 1")
  print("¡Hola Mundo!")

  print("\nEjercicio 2")
  holamundo = "¡Hola Mundo!"
  print(holamundo)

  print("\nEjercicio 3")
  nombre = input("Escriba su nombre: ")
  print(f"¡Hola {nombre}!")

  print("\nEjercicio 4")
  print("el resultado de (3+2/2*5)^2")
  resultado = ((3+2)/(2*5))**2
  print(resultado)

  print("\nEjercicio 5")
  horastrabajadas = int(input("¿Cuantas horas de trabajo tuviste? "))
  valorporhoras = int(input("valor de los horas trabajadas: "))
  valorporhoras *= horastrabajadas
  print(f"el total de sus horas es de {horastrabajadas} y su paga es de {valorporhoras}$")

  print("\nEjercicio 6")
  n = int(input("escriba el valor de n: "))
  i = 1 
  for i in range(1, n+1):
    suma = ((i*(i+1))/2)
    print("Para ", i, ": ", suma)
    i += 1

  print("\nEjercicio 7")
  peso = int(input("Su peso en KG: "))
  estatura = float(input("Su estatura en m2: "))
  imc = peso / estatura
  print(f"Su masa muscular es igual a ", round(imc, 2), " Kg/m2")

  print("\nEjercicio 8")
  n = int(input("Introduzca un numero a dividir: "))
  m = int(input("Introduzca un numero de divisor: "))
  
    
    
if __name__ == '__main__':
  hola()