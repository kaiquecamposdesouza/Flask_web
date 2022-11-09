from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Combate', 'Luta', 'PS2')
    lista_jogos = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='leandro', jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='novo jogo')

app.run(debug=True)