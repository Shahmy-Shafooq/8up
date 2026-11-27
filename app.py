from flask import Flask, render_template
from products import products_bp

app = Flask(__name__)
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)