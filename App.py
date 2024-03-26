from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="User",
    password="123",
    database="Usuarios"
)

cursor = conexao.cursor()

@app.route('/')
def login():
    return render_template('pagina.html')

@app.route('/login', methods=['POST'])
def login_post():
    login = request.form['Login']
    senha = request.form['Senha']

    cursor.execute("select * from Usuarios where Login = %s AND Senha = %s", (login, senha))
    usuario = cursor.fetchone()

    if usuario:
        return render_template('login_efetuado.html', usuario=login)
    else:
        return "<h2>Usuário ou senha incorretos.<h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)