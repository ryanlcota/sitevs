from flask import Flask, render_template

app = Flask(__name__)

# criar a 1 pagina do site

@app.route("/")
def homapage():
    return render_template("homepage.html")
# colocar o site no ar
@app.route('/contatos')
def contatos():
    return render_template("contatos.html")

@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__ == '__main__':
    app.run(debug=True)