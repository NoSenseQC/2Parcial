
function validaFormulario() {
    let js_curp = getTextInputById("curp");
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
