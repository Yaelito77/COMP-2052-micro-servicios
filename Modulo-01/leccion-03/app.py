from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de usuarios en memoria
usuarios = []

# GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "app": "Gestión de Usuarios",
        "nombre": "Yael Maldonado",
        "endpoints": ["/info", "/crear_usuario", "/usuarios"]
    })

# POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Faltan nombre o correo"}), 400

    usuario = {
        "nombre": nombre,
        "correo": correo
    }
    usuarios.append(usuario)

    return jsonify({
        "mensaje": "Usuario creado con éxito",
        "usuario": usuario
    }), 201

# GET /usuarios
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)
