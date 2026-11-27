from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

products_bp = Blueprint("products", __name__)

def get_db():
    conn = sqlite3.connect("8up.db")
    conn.row_factory = sqlite3.Row
    return conn

@products_bp.route("/products/new", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]
        category = request.form["category"]
        seller_id = 1  # fake seller
        conn = get_db()
        conn.execute(
            "INSERT INTO products (seller_id, title, description, price, category) VALUES (?, ?, ?, ?, ?)",
            (seller_id, title, description, price, category),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    return render_template("product_form.html")