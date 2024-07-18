import model.package_model.Database as Database

class Administradores:
    def __init__(self, admin='', contrasena=''):
        self.__admin = admin
        self.__contrasena = contrasena
        
    def obtener_administradores(self):
        conexion = Database.Database()
        administradores = []
        try:
            with conexion.conn.cursor() as cursor:
                cursor.execute("SELECT nombre_admin, contraseña FROM administradores")
                administradores = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener administradores: {e}")
        finally:
            conexion.conn.close()
        
        return list(administradores)
    
    @staticmethod
    def verifica_administrador(admin, contrasena):
        conexion = Database.Database()
        try:
            with conexion.conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) AS cuantos FROM administradores WHERE nombre_admin = %s AND contraseña = %s", (admin, contrasena))
                cuantos = cursor.fetchone()
                return cuantos[0]
        except Exception as e:
            print(f"Error al verificar administrador: {e}")
        finally:
            conexion.conn.close()
    
    def obtener_datos_administrador(self, admin, contrasena):
        conexion = Database.Database()
        datos_admin = None
        try:
            with conexion.conn.cursor() as cursor:
                cursor.execute("SELECT nombre_admin FROM administradores WHERE nombre_admin = %s AND contraseña = %s", (admin, contrasena))
                datos_admin = cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener datos del administrador: {e}")
        finally:
            conexion.conn.close()
        
        return datos_admin
