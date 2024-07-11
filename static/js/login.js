function validateForm() {
    var username = document.getElementById('admin-user').value;
    var password = document.getElementById('admin-password').value;

    if (username.trim() === '' || password.trim() === '') {
        alert('Por favor ingrese usuario y contraseña.');
        return false;
    }

    return true;
}