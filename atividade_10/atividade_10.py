from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
db = SQLAlchemy(app)


class Cadastro(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True)
    password = db.Column(db.String(255))


    def __init__(self, nome, password):
        self.nome = nome
        self.password = password


    def __repr__(self):
        return '<Nome %r>' % self.nome


db.create_all()


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/add')
def adiconar():
    test = Cadastro(nome='fulano', password='bbb')
    db.session.add(test)
    db.session.commit()
    result = "Usuário Cadastro"
    return result


@app.route('/del/<int:id>')
def excluir(id):
    cadastro = Cadastro.query.get(id)
    db.session.delete(cadastro)
    db.session.commit()
    return "Usuário Removido"


@app.route('/list')
def list():
    cadastro = Cadastro.query.order_by(Cadastro.id).all()
    lista = "<h1>Usuários</h1><br><ul>"
    for cadastro in cadastro:
        lista += '<p>'
        lista += 'Id = '  + str(cadastro.id)
        lista += ' Nome = ' + cadastro.nome
        lista += ' Senha = ' + cadastro.password
        lista += '</p>'
    return lista


@app.route('/find/<int:id>')
def find(id):
    cadastro = Cadastro.query.get(id)
    result = "<h1>Usuário Encontrado</h1><br><ul>"
    result += "<p> Id=" + str(cadastro.id) + "</p>"
    result += "<p> Nome=" + cadastro.nome + "</p>"
    result += "<p> Senha=" + cadastro.password + "</p>"
    return result


@app.route('/change/<int:id>')
def change(id):
    cadastro = Cadastro.query.get(id)
    cadastro.nome = 'Ciclano'
    db.session.commit()
    return 'Usuário Mudado'


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)
