from flask import Flask, render_template
import csv
import re

app = Flask(__name__)

def carregar_musicas():
    musicas = []
    with open("musicas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            musicas.append(row)
    return musicas

def chave_ordenacao(m):
    nome = m.get("musica", "").lower()
    nome = re.sub(r'^[^a-z]+', '', nome)
    return nome

TODAS_MUSICAS = sorted(carregar_musicas(), key=chave_ordenacao)

@app.route("/")
def home():
    return render_template(
        "index.html",
        musicas=TODAS_MUSICAS,
        total_banco=len(TODAS_MUSICAS)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)