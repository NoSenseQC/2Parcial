document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login').addEventListener('submit', function(e) {
        e.preventDefault();
        
        var js_us = document.getElementById("admin-user").value.trim();
        var js_pw = document.getElementById("admin-password").value.trim();
        var reresponse = grecaptcha.getResponse();

        if (js_us.length == 0 || js_pw.length == 0) {
            alert('El usuario y contraseña no deben ir vacíos');
            return false;
        } else if (js_us.length < 5 || js_pw.length < 5) {
            alert('El usuario y contraseña deben contener al menos 5 caracteres');
            return false;
        } else if (reresponse.length == 0) {
            alert('Marque la casilla de verificación de seguridad');
            return false;
        } else {
            fetch('/admin_login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ admin: js_us, contrasena: js_pw })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Mensaje de depuración para ver la respuesta
                if (data.status === 'error') {
                    alert(data.message);
                } else {
                    alert('Bienvenido');
                    window.location.href = "/admin_menu";  // Redirige al menú de administrador
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error en el servidor: ' + error);
            });
        }
    });
});
