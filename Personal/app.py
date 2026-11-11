from flask import Flask, render_template
#necesario para la aplicacion de flas funcione ojo solo puedes dejar el __name__ pero por defecto la carpeta se deberia de llamar templates para que funcione
app = Flask(__name__,template_folder ="pestanitas")
#es como si indicaras a cual pestaña vas a ir por defecto 
@app.route("/")
def login():
    #aqui va el nombre del html a donde quieres ir
    return render_template("login.html")
#inicia los servidores de flask
if __name__ == "__main__":
    app.run(debug=True)
