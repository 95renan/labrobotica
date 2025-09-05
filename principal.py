from flask import Flask, render_template

#Criando a aplicação
app = Flask(__name__)

#Definição das rotas
@app.route('/')
def hello_world():
    return render_template('teste.html')

@app.route('/renan')
def hello():
    return '<h1> Olá Renan! O nome do seu projeto integrador é Meu Neto!</h1>'

#Definição da pagina principal
if __name__ == '__main__': 
    app.run (debug=True)