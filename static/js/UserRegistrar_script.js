function validaFormulario() {
    let js_curp = getTextInputById("curp");
    let js_solicitante = getTextInputById("solicitante");
    let js_nombre = getTextInputById("nombre");
    let js_paterno = getTextInputById("paterno");
    let js_materno = getTextInputById("materno");
    let js_telefono = getTextInputById("telefono");
    let js_celular = getTextInputById("celular");
    let js_correo = getTextInputById("correo");
    let js_nivel = document.getElementById("nivel").value;
    let js_municipio = document.getElementById("municipio").value;
    let js_asunto = document.getElementById("asunto").value;
    let js_modificarCurp = getTextInputById("modificar-curp");
    let js_numeroTurno = getTextInputById("numero-turno");

    // Validación para CURP
    if (!validarCURP(js_curp)) {
        alert("El CURP ingresado no es válido");
        return false;
    }
    if (js_solicitante.trim().length === 0) {
        alert("El nombre del solicitante es obligatorio");
        return false;
    }
    if (js_nombre.trim().length === 0) {
        alert("El campo nombre es obligatorio");
        return false;
    }
    if (js_paterno.trim().length === 0) {
        alert("El campo paterno es obligatorio");
        return false;
    }
    if (js_materno.trim().length === 0) {
        alert("El campo materno es obligatorio");
        return false;
    }
    if (js_telefono.trim().length === 0 && js_celular.trim().length === 0) {
        alert("Debe ingresar al menos un teléfono o celular");
        return false;
    }
    if (js_correo.trim().length === 0) {
        alert("El campo correo es obligatorio");
        return false;
    }
    if (js_nivel.trim().length === 0) {
        alert("Debe seleccionar un nivel");
        return false;
    }
    if (js_municipio.trim().length === 0) {
        alert("Debe seleccionar un municipio");
        return false;
    }
    if (js_asunto.trim().length === 0) {
        alert("Debe seleccionar un asunto");
        return false;
    }

    // Validaciones adicionales para modificar solicitud
    if (js_modificarCurp.trim().length === 0 || js_numeroTurno.trim().length === 0) {
        alert("Para modificar la solicitud, debe ingresar la CURP y el número de turno asignado");
        return false;
    }

    // Si todas las validaciones son correctas, se puede enviar el formulario
    return true;
}

function validarCURP(curp) {
    // Expresión regular para validar CURP (formato básico, puedes ajustarlo según necesites)
    let regex = /^[A-Z]{4}[0-9]{6}[H|M][A-Z]{5}[0-9]{2}$/;
    return regex.test(curp);
}

let getTextInputById = (id) => {
    return document.getElementById(id).value;
};

function buscarSolicitud() {
    const curp = document.getElementById('buscar-curp').value;
    const turno = document.getElementById('buscar-turno').value;
    // Aquí iría la llamada al backend para buscar la solicitud

    // Simulación de datos encontrados
    const solicitudEncontrada = {
        curp: curp,
        turno: turno,
        nombre: 'Nombre Ejemplo',
        paterno: 'Apellido Paterno',
        materno: 'Apellido Materno',
        telefono: '1234567890',
        celular: '0987654321',
        correo: 'ejemplo@correo.com',
        nivel: 'preparatoria',
        municipio: 'municipio1',
        asunto: 'asunto1'
    };

    // Si se encuentra la solicitud, se rellenan los campos del formulario de modificación
    document.getElementById('modificar-solicitud-form').style.display = 'block';
    document.getElementById('modificar-curp').value = solicitudEncontrada.curp;
    document.getElementById('modificar-turno').value = solicitudEncontrada.turno;
    document.getElementById('modificar-nombre').value = solicitudEncontrada.nombre;
    document.getElementById('modificar-paterno').value = solicitudEncontrada.paterno;
    document.getElementById('modificar-materno').value = solicitudEncontrada.materno;
    document.getElementById('modificar-telefono').value = solicitudEncontrada.telefono;
    document.getElementById('modificar-celular').value = solicitudEncontrada.celular;
    document.getElementById('modificar-correo').value = solicitudEncontrada.correo;
    document.getElementById('modificar-nivel').value = solicitudEncontrada.nivel;
    document.getElementById('modificar-municipio').value = solicitudEncontrada.municipio;
    document.getElementById('modificar-asunto').value = solicitudEncontrada.asunto;

    return false; // Prevenir el envío del formulario de búsqueda
}
