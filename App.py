from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify, session
import model.package_model.Administradores as Administradores_o
import model.package_model.Municipio as Municipio_o  # Importar el modelo de Municipio
import model.package_model.Asunto as Asunto_o  # Importar el modelo de Asunto
import model.package_model.Nivel as Nivel_o  # Importar el modelo de Nivel
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
import random  # Para generar números de turno simulados

# Importar métodos estáticos
from model.package_model.Administradores import Administradores

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para utilizar sesiones

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
    try:
        data = request.get_json()  # obtener datos de la solicitud JSON
        if data is None:
            raise ValueError("No se recibieron datos JSON")
        admin = data['admin']
        contrasena = data['contrasena']
        if admin.strip() == '' or contrasena.strip() == '':
            return jsonify({'status': 'error', 'message': 'El usuario y la contraseña no deben ir vacíos'})

        existe = Administradores.verifica_administrador(admin, contrasena)
        if existe:
            session['admin_id'] = admin
            return jsonify({'status': 'success', 'message': 'Autenticación exitosa'})
        else:
            return jsonify({'status': 'error', 'message': 'Nombre de usuario o contraseña incorrectos'})
    except Exception as e:
        print(f"Error en admin_login: {e}")
        return jsonify({'status': 'error', 'message': 'Error en el servidor: ' + str(e)})

@app.route('/admin_menu')
def admin_menu():
    return render_template('AdminMenu.html')

@app.route('/admin_consulta')
def admin_consulta():
    return render_template('AdminConsulta.html')

@app.route('/admin_catalogos')
def admin_catalogos():
    return render_template('AdminCatalogos.html')

@app.route('/User_Registrar', methods=['GET', 'POST'])
def user_registrar():
    municipio_model = Municipio_o.Municipio()  # Crear instancia del modelo Municipio
    asuntos_model = Asunto_o.Asunto()  # Crear instancia del modelo Asunto
    niveles_model = Nivel_o.Nivel()  # Crear instancia del modelo Nivel
    municipios = municipio_model.obtener_municipios()  # Obtener lista de municipios
    asuntos = asuntos_model.obtener_asuntos()  # Obtener lista de asuntos
    niveles = niveles_model.obtener_niveles()  # Obtener lista de niveles
    if request.method == 'POST':
        # Obtener datos del formulario
        curp = request.form['curp']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        telefono = request.form['telefono']
        celular = request.form['celular']
        correo = request.form['correo']
        nivel = request.form['nivel']
        municipio = request.form['municipio']
        asunto = request.form['asunto']

        # Generar número de turno simulado
        numero_turno = random.randint(1000, 9999)  # Número de turno aleatorio de 4 dígitos

        # Generar PDF
        pdf_buffer = generar_pdf(curp, nombre, paterno, materno, numero_turno)

        # Generar QR
        generar_qr(curp)

        return send_file(pdf_buffer, as_attachment=True, download_name='solicitud.pdf', mimetype='application/pdf')

    return render_template('UserRegistrar.html', municipios=municipios, asuntos=asuntos, niveles=niveles)  # Pasar municipios, asuntos y niveles a la plantilla

def generar_pdf(curp, nombre, paterno, materno, numero_turno):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, "Solicitud de Registro")
    c.drawString(100, 730, f"Nombre: {nombre} {paterno} {materno}")
    c.drawString(100, 710, f"CURP: {curp}")
    c.drawString(100, 690, f"Turno Asignado: {numero_turno}")
    c.save()

    buffer.seek(0)
    return buffer

def generar_qr(curp):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(curp)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/qrcode.png")

if __name__ == '__main__':
    app.run(debug=True)
