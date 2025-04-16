from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "app": "Test de Flask",
        "Nombre": "Yael Maldonado"
    })

# Ruta POST /mensaje
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.get_json()
    if not data or "mensaje" not in data:
        return jsonify({"error": "Falta el campo 'mensaje'"}), 400

    mensaje_recibido = data["mensaje"]
    respuesta = f"Recibí tu mensaje: '{mensaje_recibido}'"
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
