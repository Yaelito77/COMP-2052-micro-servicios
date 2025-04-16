from flask import Flask, render_template

app = Flask(__name__)

# Datos simulados
productos = [
    {"id": 1, "nombre": "RTX 5070", "precio": 850.99},
    {"id": 2, "nombre": "Ryzen 9 7900x", "precio": 349.99}
]

usuarios = [
    {"id": 1, "nombre": "Saul"},
    {"id": 2, "nombre": "Janiel"}
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
