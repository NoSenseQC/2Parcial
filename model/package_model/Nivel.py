import model.package_model.Database as Database
import pymysql

class Nivel:
    def __init__(self, id_nivel='', n_nivel=''):
        self.__id_nivel = id_nivel
        self.__n_nivel = n_nivel
        
    def obtener_niveles(self):
        conexion = Database.Database()
        niveles=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_NIVEL,NIVEL FROM nivel"
            cursor.execute(sql)
            niveles = cursor.fetchall()
        conexion.close()
        return niveles
    
    def obtener_nivel_por_id(self, id_nivel):
        conexion = Database.Database()
        nivel=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_NIVEL,NIVEL FROM nivel WHERE ID_NIVEL = %s"
            cursor.execute(sql,(id_nivel))
            nivel = cursor.fetchone()
        conexion.close()
        return nivel
    
    def agregar_nivel(self, obj_niv):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql ="INSERT INTO nivel(NIVEL) VALUES(%s)"
                vals=(obj_niv.__n_nivel)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
           
    def eliminar_nivel(self, id_nivel):
        conexion = Database.Database()
        affected = 0;
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM nivel WHERE ID_NIVEL = %s"
                vals=(id_nivel)
                affected=cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
 
    def modificar_nivel(self, obj_niv):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE nivel SET NIVEL = %s WHERE ID_NIVEL = %s"
                vals=(obj_niv.__n_nivel, obj_niv.__id_nivel)
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
    def existe_nivel(nom):
        conexion = Database.Database()
        nivel = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM nivel WHERE NIVEL = %s"
            vals=(nom)
            cursor.execute(sql,vals)
            nivel = cursor.fetchone()
        conexion.close()
        return nivel[0]