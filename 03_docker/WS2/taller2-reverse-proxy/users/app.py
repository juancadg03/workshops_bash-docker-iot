from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "service": "users",
        "message": "Servicio de usuarios"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
