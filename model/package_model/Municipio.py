import model.package_model.Database as Database
import pymysql
class Municipio:
    def __init__(self,id_municipio='', nombre_municipio=''):
        self.__id_municipio = id_municipio
        self.__nombre_municipio = nombre_municipio
        
    def obtener_municipios(self):
        conexion = Database.Database()
        municipios=[]
        with conexion.cursor as cursor:
            sql = "SELECT ID_MUNICIPIO,MUNICIPIO FROM municipio"
            cursor.execute(sql)
            municipios = cursor.fetchall()
        conexion.close()
        return municipios
    
    def obtener_municipio_por_id(self,id_municipio):
        conexion = Database.Database()
        municipio = []
        with conexion.cursor as cursor:
            sql = "SELECT ID_MUNICIPIO,MUNICIPIO FROM municipio WHERE ID_MUNICIPIO = %s"
            cursor.execute(sql,(id_municipio))
            municipio = cursor.fetchone()
        conexion.close()
        return municipio
        
    def agregar_municipio(self, obj_mun):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "INSERT INTO municipio(MUNICIPIO) VALUES(%s)"
                vals = (obj_mun.__nombre_municipio)
                affected = cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
    
    def eliminar_municipio(self, id_municipio):
        conexion = Database.Database()
        affected = 0
        with conexion.cursor as cursor:
            try:
                sql = "DELETE FROM municipio WHERE ID_MUNICIPIO = %s"
                vals = (id_municipio)
                affected = cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    def modificar_municipio(self, obj_mun):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                sql = "UPDATE municipio SET MUNICIPIO = %s WHERE ID_MUNICIPIO = %s"
                vals = (obj_mun.__nombre_municipio,obj_mun.__id_municipio)
                affected = cursor.execute(sql,vals)
                conexion.conn.commit()
                return affected
            except Exception as e:
                return e
            except pymysql.err.ProgrammingError as except_detail:
                return print("pymysql.err.ProgrammingError: {0}".format(except_detail))
            finally:
                conexion.conn.close()
                
    @staticmethod
    def existe_municipio(nom):
        conexion = Database.Database()
        municipio = None
        with conexion.cursor as cursor:
            sql = "SELECT count(*) as ex FROM municipio WHERE MUNICIPIO = %s"
            vals = (nom)
            cursor.execute(sql,vals)
            municipio = cursor.fetchone()
        conexion.close()
        return municipio[0]