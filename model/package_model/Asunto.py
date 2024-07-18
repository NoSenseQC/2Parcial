import model.package_model.Database as Database
import pymysql

class Asunto:
    def __init__(self, id_asunto='', n_asunto=''):
        self.__id_asunto = id_asunto
        self.__n_asunto = n_asunto
        
    def obtener_asuntos(self):
        conexion = Database.Database()
        asuntos=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_ASUNTO,ASUNTO FROM asunto"
            cursor.execute(sql)
            asuntos = cursor.fetchall()
        conexion.close()
        return asuntos
    
    def obtener_asunto_por_id(self, id_asunto):
        conexion = Database.Database()
        asunto=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_ASUNTO,ASUNTO FROM asunto WHERE ID_ASUNTO = %s"
            cursor.execute(sql,(id_asunto))
            asunto = cursor.fetchone()
        conexion.close()
        return asunto
    
    def agregar_asunto(self, obj_asu):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql ="INSERT INTO asunto(ASUNTO) VALUES(%s)"
                vals=(obj_asu.__n_asunto)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    def eliminar_asunto(self, id_asunto):
        conexion = Database.Database()
        affected = 0;
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM asunto WHERE ID_ASUNTO = %s"
                vals=(id_asunto)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    def modificar_asunto(self, obj_asu):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE asunto SET ASUNTO = %s WHERE ID_ASUNTO = %s"
                vals=(obj_asu.__n_asunto, obj_asu.__id_asunto)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    @staticmethod
    def existe_asunto(nom):
        conexion = Database.Database()
        asunto = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM asunto WHERE ASUNTO = %s"
            vals=(nom)
            cursor.execute(sql,vals)
            asunto = cursor.fetchone()
        conexion.close()
        return asunto[0]