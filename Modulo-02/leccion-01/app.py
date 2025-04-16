from flask import Flask, render_template

app = Flask(__name__)

# Datos simulados
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1000},
    {"id": 2, "nombre": "Mouse", "precio": 25}
]

usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"}
]

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/productos")
def mostrar_productos():
    return render_template("productos.html", productos=productos)

@app.route("/usuarios")
def mostrar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
