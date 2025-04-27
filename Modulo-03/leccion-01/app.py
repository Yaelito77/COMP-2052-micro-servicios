from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configurando Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Usuario de ejemplo
class User(UserMixin):
    def __init__(self, id, username, password_hash, role):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role

# Base de datos simulada
users = {
    "Saul": User(1, "Saul", generate_password_hash("1234"), "admin"),
    "Janiel": User(2, "Janiel", generate_password_hash("abcd"), "user")
}

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.id) == user_id:
            return user
    return None

# Ruta de inicio
@app.route('/')
def index():
    return "Bienvenido a mi aplicación. <a href='/login'>Iniciar sesión</a>"

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Usuario o contraseña incorrectos. <a href='/login'>Intentar de nuevo</a>"

    return '''
        <form method='post'>
            Usuario: <input type='text' name='username'><br>
            Contraseña: <input type='password' name='password'><br>
            <input type='submit' value='Iniciar sesión'>
        </form>
    '''

# Ruta protegida
@app.route('/dashboard')
@login_required
def dashboard():
    return f"Hola, {current_user.username}! Tu rol es: {current_user.role}. <a href='/logout'>Cerrar sesión</a>"

# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "sesión cerrada. <a href='/login'>Iniciar sesión de nuevo</a>"

if __name__ == '__main__':
    app.run(debug=True)
