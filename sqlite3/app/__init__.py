import sqlite3

print('''1.agregar \n2.buscar ''')
opc = input()
db = sqlite3.connect('prueba')

if opc == '1':

    cursor = db.cursor()
    autor = input('autor: ')
    cpag = input('introdusca la cantidad de paginas del libro: ')
    public = input('fecha de publicacion: ')
    cursor.execute('''INSERT INTO libro (autor,cpag,public )VALUES(?,?,?)''', (autor, cpag, public))

elif opc == '2':
    db = sqlite3.connect('prueba')
    cursor = db.cursor()
    bus = input('escriba el nombre del autor: ')
    r = cursor.execute('SELET autor FROM libro where autor = ?', (bus))
    print(r)



db.commit()
db.close()



