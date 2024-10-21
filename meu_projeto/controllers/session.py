from flask import Flask, session, redirect, url_for, request, Blueprint
from models.usuarios import listUsers
app = Flask(__name__)
app.secret_key = "sua-chave-secreta"

usuarios=[
    
]


@app.route('/')
def index():
    if 'username' in session:
        return f"Bem-vindo, {session['username']}!"
    else:
        return "Você não está logado. <a href='/login'>Faça login</a>."

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Nome de usuário: <input type="text" name="username">
            Senha: <input type="password" name="senha">
            <input type="submit">
            
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
