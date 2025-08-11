from flask import Flask, render_template, request
from modelo import prever_probabilidade


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        dados = {
            "genero": request.form["genero"],
            "idade": request.form["idade"],
            "hipertensao": request.form["hipertensao"],
            "cardiaca": request.form["cardiaca"],
            "casado": request.form["casado"],
            "trabalho": request.form["trabalho"],
            "residencia": request.form["residencia"],
            "glicose": request.form["glicose"],
            "imc": request.form["imc"],
            "fumante": request.form["fumante"]
        }


        probabilidade = prever_probabilidade(dados)

        return render_template("resultado.html", dados=dados, probabilidade=probabilidade)

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
