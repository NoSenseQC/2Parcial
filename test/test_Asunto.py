#import model.package_model.Asunto as Asunto
from model.package_model.Asunto import Asunto

# obj_asunto = Asunto.Asunto()

# lista_asuntos = obj_asunto.obtener_asuntos()

# if lista_asuntos!=None:
#     for x in lista_asuntos:
#         print(x)
# else:
#     print("No hay registros")
    
# print("\n=====================================\n")

# asunto_id = obj_asunto.obtener_asunto_por_id(1)
# print(asunto_id)

# print("\n======INSERTADO===========\n")
# id=0
# nom='edsades'
# if len(nom)>2:
#     obj_asunto_new=Asunto.Asunto(id,nom)
#     result_ins=obj_asunto.agregar_asunto(obj_asunto_new)
    
#     if result_ins==1:
#         print("Registro insertado")
#     else:
#         print("Error al insertar")
# else:
#     print("Nombre no valido")
    
# print("\n======borrado===========\n")
# id = 4
# result_del=obj_asunto.eliminar_asunto(id)
# if result_del==1:
#     print("Registro eliminado")
# else:
#     print("Error al eliminar")
    
# print("\n======update===========\n")
# id=4
# nom='nombre mdoficiado'
# if len(nom)>2:
#     obj_asunto_new=Asunto.Asunto(id,nom)
#     result_upd=obj_asunto.modificar_asunto(obj_asunto_new)
    
#     if result_upd==1:
#         print("Registro modificado")
#     else:
#         print("Error al modificar")
# else:
#     print("Nombre no valido")
    
cuantos = Asunto.existe_asunto('Consulta de expediente')
print (cuantos)