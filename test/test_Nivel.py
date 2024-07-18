import model.package_model.Nivel as Nivel
#from model.package_model.Nivel import Nivel

obj_nivel = Nivel.Nivel()
lista_niveles = obj_nivel.obtener_niveles()
 
if lista_niveles!=None:
    for x in lista_niveles:
        print(x)
else:
    print("No hay registros")

print("\n=====================================\n")

nivel_id = obj_nivel.obtener_nivel_por_id(1)
print(nivel_id)

print("\n======INSERTADO===========\n")
id=0
nom='edsades'
if len(nom)>2:
    obj_nivel_new=Nivel.Nivel(id,nom)
    result_ins=obj_nivel.agregar_nivel(obj_nivel_new)
    
    if result_ins==1:
        print("Registro insertado")
    else:
        print("Error al insertar")
else:
    print("Nombre no valido")
    
print("\n======borrado===========\n")
id = 4
result_del=obj_nivel.eliminar_nivel(id)
if result_del==1:
    print("Registro eliminado")
else:
    print("Error al eliminar")
    
print("\n======update===========\n")
id=4
nom='nombre mdoficiado'
if len(nom)>2:
    obj_nivel_new=Nivel.Nivel(id,nom)
    result_upd=obj_nivel.modificar_nivel(obj_nivel_new)
    
    if result_upd==1:
        print("Registro modificado")
    else:
        print("Error al modificar")
else:
    print("Nombre no valido")
    
cuantos = Nivel.existe_Nivel('nombre mdoficiado')
print (cuantos)