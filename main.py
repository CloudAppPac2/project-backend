"""
Moduł flask
"""
from flask import Flask, render_template, request

main = Flask(__name__)


@main.route("/")
def index():
    """
       Funkcja wyświetla napis "Hello World"

       """
    return "Hello, world!"


@main.route("/hello", methods=["GET", "POST"])
def hello():
    """
       Funkcja "/hello" wyświetla formularz z polem, które umożliwia wpisanie imienia.
       Po przesłaniu, aplikacja wyświetli "Hello, (name)!".

       """
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("hello.html")


if __name__ == "__main__":
    main.run(debug=True, host="0.0.0.0", port=8000)
