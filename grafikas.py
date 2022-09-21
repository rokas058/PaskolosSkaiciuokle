from flask import Flask, render_template, request
from main import Paskola


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        suma = int(request.form.get('suma'))
        palukanos = int(request.form.get('palukanos'))
        terminas = int(request.form.get('terminas'))
        file = Paskola(suma, palukanos, terminas).mokejimo_grafikas()
        return render_template("grafikas.html", tables=[file.to_html()], titles=[''])
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
