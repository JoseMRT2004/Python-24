from modules import conexion 

conetar_SQL = conexion.conection

cursor = conetar_SQL.cursor()

def registrar_User():
   NOMBRE = input('Igrese su nombre: ').lower()
   APELLIDO = input('Igrese su apellido: ').lower()
   
   consulta = "insert into Usuarios (nombre,apellido) values (?,?)"
   valores = (NOMBRE,APELLIDO) 
   cursor.execute(consulta,valores)
   cursor.commit()
   
   if (cursor.execute):
       print('Insertado con exito por GOAT')
   else:
       print('Usuario denegado por PUTO')
       
registrar_User()    