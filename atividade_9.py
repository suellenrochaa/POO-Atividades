from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Alô Mundo ! Aqui é a Suellen testando o Flask !'

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)