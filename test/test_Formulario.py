from model.package_model.Formulario import Formulario

# Datos para el nuevo formulario
no_turno = '4'
n_solicitante = 'Solicitante 1'
curp = 'ABC123456789XYZ'
nombre = 'Juan'
paterno = 'Perez'
materno = 'Gomez'
telefono = '5551234567' 
celular = '5559876543'
correo = 'juan.perez@example.com'
id_nivel = 1
id_mun = 1
id_asunto = 1


# Verificar si el formulario existe
if len(no_turno) > 0:
    cuantos = Formulario.existe_formulario(no_turno)
    if cuantos == 0:
        # Insertar nuevo formulario
        formulario = Formulario(no_turno, n_solicitante, curp, nombre, paterno, materno, telefono, celular, correo, id_nivel, id_mun, id_asunto)
        result_ins = formulario.insertar_formulario(formulario)
        if result_ins == '1':
            print("Registro insertado correctamente")
        else:
            print("Registro no insertado correctamente")
    else:
        print("El número de turno ya existe")
else:
    print("El número de turno debe tener al menos 1 carácter")

# # Obtener y mostrar todos los formularios
# formularios = Formulario().obtener_formularios()
# print("Todos los formularios:", formularios)

# # Obtener y mostrar un formulario específico
# formulario_especifico = Formulario.obtener_formulario_por_no_turno(no_turno)
# print("Formulario específico:", formulario_especifico)

# # Actualizar un formulario existente
# nuevo_nombre = 'Juan Actualizado'
# formulario_actualizado = Formulario(no_turno, n_solicitante, curp, nuevo_nombre, paterno, materno, telefono, celular, correo, id_nivel, id_mun, id_asunto)
# result_upd = Formulario().actualizar_formulario(formulario_actualizado)
# if result_upd == 1:
#     print("Registro actualizado correctamente")
# else:
#     print("Registro no actualizado correctamente")

# # Eliminar un formulario
# result_del = Formulario().eliminar_formulario(no_turno)
# if result_del == 1:
#     print("Registro eliminado correctamente")
# else:
#     print("Registro no eliminado correctamente")
