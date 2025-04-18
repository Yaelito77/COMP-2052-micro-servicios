from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistroForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-super-segura'
csrf = CSRFProtect(app)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        flash('¡Registro exitoso!', 'success')
        return redirect(url_for('registro'))
    return render_template('registro.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
