from flask import Flask, request, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, AnonymousIdentity, identity_changed, identity_loaded
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configuración de Flask-Principal
principal = Principal(app)

# Definición de permisos
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Usuario de ejemplo
class User(UserMixin):
    def __init__(self, id, username, password_hash, role):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role

# Base de datos simulada
users = {
    "Yael": User(1, "Yael", generate_password_hash("holayael"), "admin"),
    "Agustino": User(2, "Agustino", generate_password_hash("holaagustino"), "user")
}

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.id) == user_id:
            return user
    return None

# Manejar la identidad
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if current_user.is_authenticated:
        identity.provides.add(RoleNeed(current_user.role))

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos.")

    return render_template('login.html')

# Ruta protegida para usuarios logeados
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Ruta protegida para admin
@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin_panel():
    return render_template('admin_panel.html')

# Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('index'))

# Manejador de error 403
@app.errorhandler(403)
def acceso_denegado(e):
    return render_template('error_403.html'), 403

if __name__ == '__main__':
    app.run(debug=True)
