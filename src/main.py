from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from os.path import join, dirname




dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SECRET = ('SECRET_KEY_SOCKET')
SECRET_KEY = os.environ.get(SECRET)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app, cors_allowed_origins = "*")

@app.route('/') #   Cliente Index
def index():
    return render_template('index.html')

@socketio.on('connection')  #   Cliente Conectado
def handleConnect(socket):

    print('Usuario Conectado', socket)
    emit('connection', socket)

@socketio.on('disconnect')  #   Cliente Desconectado
def test_disconnect():
    print('Cliente Desconectado')

@socketio.on('chat message')    #   Mensaje Directo al Servidor
def handleMessage(msg):
    print('Message: ', msg)
    emit('chat message', msg)

@socketio.on('chat message')    #   Mensaje Cliente a Cliente
def handleExchange(data):
    #print('chat message', data)
    emit('chat message', data, broadcast=True)

if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app)