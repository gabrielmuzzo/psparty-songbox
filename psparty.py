from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

def carregar_musicas():
    musicas = []
    with open("musicas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            musicas.append(row)
    return musicas

TODAS_MUSICAS = carregar_musicas()

@app.route("/")
def home():
    return render_template(
        "index.html",
        total_banco=len(TODAS_MUSICAS)
    )

@app.route("/buscar")
def buscar():
    termo = request.args.get("q", "").lower()

    resultados = []

    if termo:
        for m in TODAS_MUSICAS:
            if termo in m["artista"].lower() or termo in m["musica"].lower():
                resultados.append(m)

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)