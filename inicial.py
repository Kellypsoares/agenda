
from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
   


@app.route("/<mensagem>")
def hello_world2(mensagem):
    return f"<p>Hello, World! {mensagem}</p>"




if __name__ == '__main__':
    app.run()