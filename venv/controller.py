from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combate', 'Luta', 'PS2')
lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('lista.html', titulo='leandro', jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='novo jogo')

@app.route('/criar',  methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


app.run(debug=True)