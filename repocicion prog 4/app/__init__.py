import sqlite3
print("\n")
print("bienvenido a la captacion de datos")
print('''1.agregar datos de persona \n2.agregar datos de familia ''')
opc = input()
P = "si"
if opc == '1':
 while P == 'si':
    print("\n")
    print("datos de la tabla persona")
    conexion = sqlite3.connect('tarea2.db')
    cursor = conexion.cursor()
    cedula = input(" cedula: ")
    nombre = input(" nombre: ")
    apellido = input(" apellido: ")
    Lnacimiento = input(" lugar de nacimiento: ")
    Anacimiento = input(" años de nacimiento:")
    cursor.execute('''CREATE TABLE IF NOT EXISTS persona (cedula, nombre, apellido, Lnacimiento, Anacimiento)''')
    cursor.execute('''INSERT INTO persona(cedula, nombre, apellido, Lnacimiento,Anacimiento) VALUES (?,?,?,?,?)''',
               (cedula, nombre, apellido, Lnacimiento, Anacimiento,))
    conexion.commit()
    P = input("¿desea agregar mas datos de personas si/no ?\n")


elif opc == '2':
    while P == 'si':
      conexion = sqlite3.connect('tarea2.db')
      cursor = conexion.cursor()
      print("datos de la tabla familia")
      idfamilia = input("familia: ")
      idpersona1 = input(" padres: ")
      idpersona2 = input("hijo: ")

      cursor.execute('''CREATE TABLE IF NOT EXISTS familia ( idfamilia, idpersona1, idpersona2 )''')
      cursor.execute('''INSERT INTO familia(idfamilia, idpersona1, idpersona2) VALUES (?,?,?)''',
               (idfamilia, idpersona1, idpersona2,))
      P = input("¿desea agregar mas datos de familia si/no ?\n")

      conexion.commit()


