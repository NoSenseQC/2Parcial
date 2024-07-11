from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    # Aquí puedes añadir la lógica de autenticación
    if username == 'admin' and password == 'password':  # Ejemplo básico
        return redirect(url_for('admin_menu'))
    else:
        return redirect(url_for('login'))

@app.route('/admin_menu')
def admin_menu():
    return render_template('AdminMenu.html')

@app.route('/admin_consulta')
def admin_consulta():
    return render_template('AdminConsulta.html')

@app.route('/admin_catalogos')
def admin_catalogos():
    return render_template('AdminCatalogos.html')

if __name__ == '__main__':
    app.run(debug=True)
