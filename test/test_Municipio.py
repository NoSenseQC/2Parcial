import model.package_model.Municipio as Municipio
# from model.package_model.Municipio import Municipio

obj_municipio = Municipio.Municipio()

# lista_municipios = obj_municipio.obtener_municipios()

# if lista_municipios!=None:
#     for x in lista_municipios:
#         print(x)
# else:
#     print("No hay registros")

# print("\n=====================================\n")

# municipio_id = obj_municipio.obtener_municipio_por_id(1)
# print(municipio_id)

print("\n======INSERTADO===========\n")
id=0
nom='Monterrey'
if len(nom)>2:
    obj_municipio_new=Municipio.Municipio(id,nom)
    result_ins=obj_municipio.agregar_municipio(obj_municipio_new)

    if result_ins==1:
        print("Registro insertado")
    else:
        print("Error al insertar")
else:
    print("Nombre no valido")

# print("\n======borrado===========\n")
# id = 11
# result_del=obj_municipio.eliminar_municipio(id)
# if result_del==1:
#     print("Registro eliminado")
# else:
#     print("Error al eliminar")

# print("\n======update===========\n")
# id=11
# nom='mun mdoficiado'
# if len(nom)>2:
#     obj_municipio_new=Municipio.Municipio(id,nom)
#     result_upd=obj_municipio.modificar_municipio(obj_municipio_new)

#     if result_upd==1:
#         print("Registro modificado")
#     else:
#         print("Error al modificar")
# else:
#     print("Nombre no valido")

# cuantos = Municipio.existe_municipio('Saltillo')
# print (cuantos)
