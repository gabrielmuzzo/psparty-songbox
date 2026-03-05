from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def carregar_musicas():
    musicas = []
    with open("musicas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            musicas.append(row)
    return musicas

# carrega todas as músicas uma vez
TODAS_MUSICAS = carregar_musicas()

@app.route("/", methods=["GET"])
def home():

    busca = request.args.get("busca", "").lower()

    if busca:
        musicas_filtradas = [
            m for m in TODAS_MUSICAS
            if busca in m["artista"].lower()
            or busca in m["musica"].lower()
        ]
    else:
        musicas_filtradas = TODAS_MUSICAS

    return render_template(
        "index.html",
        musicas=musicas_filtradas,
        busca=busca,
        total_banco=len(TODAS_MUSICAS)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)