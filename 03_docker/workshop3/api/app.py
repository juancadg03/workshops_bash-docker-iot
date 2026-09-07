import os
import psycopg

from flask import Flask, jsonify, request

app = Flask(__name__)


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


# GET /products
@app.route("/products", methods=["GET"])
def get_products():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM products ORDER BY id")
    rows = cur.fetchall()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        })

    cur.close()
    conn.close()

    return jsonify({
        "served_by": os.getenv("INSTANCE"),
        "products": products
    })


# GET /products/<id>
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, price FROM products WHERE id = %s",
        (id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({
        "served_by": os.getenv("INSTANCE"),
        "product": {
            "id": row[0],
            "name": row[1],
            "price": float(row[2])
        }
    })


# POST /products
@app.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name, price) VALUES (%s, %s)",
        (data["name"], data["price"])
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "served_by": os.getenv("INSTANCE"),
        "message": "Producto creado"
    }), 201


# PUT /products/<id>
@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    data = request.get_json()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE products SET name = %s, price = %s WHERE id = %s",
        (data["name"], data["price"], id)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "served_by": os.getenv("INSTANCE"),
        "message": "Producto actualizado"
    })


# DELETE /products/<id>
@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM products WHERE id = %s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "served_by": os.getenv("INSTANCE"),
        "message": "Producto eliminado"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   
