import model.package_model.Database as Database
from flask import jsonify

class Formulario:
    def __init__(self, no_turno='', n_solicitante='', curp='', nombre='', paterno='', materno='', telefono='', celular='', correo='', id_nivel=0, id_mun=0, id_asunto=0):
        self.__no_turno = no_turno
        self.__n_solicitante = n_solicitante
        self.__curp = curp
        self.__nombre = nombre
        self.__paterno = paterno
        self.__materno = materno
        self.__telefono = telefono
        self.__celular = celular
        self.__correo = correo
        self.__id_asunto = id_asunto
        self.__id_mun = id_mun
        self.__id_nivel = id_nivel
        
    @staticmethod
    def existe_formulario(no_turno):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT count(*) as ex FROM formulario WHERE NO_TURNO = %s", (no_turno,))
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario[0]
    
    def insertar_formulario(self, obj_form):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            try:
                query = "INSERT INTO formulario(NO_TURNO, NOMBRE_SOLICITANTE, CURP, NOMBRE, PATERNO, MATERNO, TELEFONO, CELULAR, CORREO, ID_NIVEL, ID_MUN, ID_ASUNTO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                vals = (obj_form.__no_turno, obj_form.__n_solicitante, obj_form.__curp, obj_form.__nombre, obj_form.__paterno, obj_form.__materno, obj_form.__telefono, obj_form.__celular, obj_form.__correo, obj_form.__id_nivel, obj_form.__id_mun, obj_form.__id_asunto)
                affected = cursor.execute(query, vals)
                conexion.conn.commit()
                return str(cursor.rowcount)
            except Exception as e:
                return str(e)
            finally:
                conexion.conn.close()
    
    def eliminar_formulario(self, no_turno):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            affected = cursor.execute("DELETE FROM formulario WHERE NO_TURNO = %s", (no_turno,))
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def actualizar_formulario(self, obj_form):
        conexion = Database.Database()
        with conexion.cursor as cursor:
            query = "UPDATE formulario SET NOMBRE_SOLICITANTE = %s, CURP = %s, NOMBRE = %s, PATERNO = %s, MATERNO = %s, TELEFONO = %s, CELULAR = %s, CORREO = %s, ID_NIVEL = %s, ID_MUN = %s, ID_ASUNTO = %s WHERE NO_TURNO = %s"
            vals = (obj_form.__n_solicitante, obj_form.__curp, obj_form.__nombre, obj_form.__paterno, obj_form.__materno, obj_form.__telefono, obj_form.__celular, obj_form.__correo, obj_form.__id_nivel, obj_form.__id_mun, obj_form.__id_asunto, obj_form.__no_turno)
            affected = cursor.execute(query, vals)
        conexion.conn.commit()
        conexion.conn.close()
        return affected
    
    def obtener_formularios(self):
        conexion = Database.Database()
        formularios = []
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario")
            formularios = cursor.fetchall()
        conexion.conn.close()
        return formularios
    
    @staticmethod
    def obtener_formulario_por_no_turno(no_turno):
        conexion = Database.Database()
        formulario = None
        with conexion.cursor as cursor:
            cursor.execute("SELECT * FROM formulario WHERE NO_TURNO = %s", (no_turno,))
            formulario = cursor.fetchone()
        conexion.conn.close()
        return formulario
