from app import app
from flask_socketio import SocketIO, send
import os


socketIo = SocketIO(app, cors_allowed_origins='*')


@socketIo.on('message')
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)

@socketIo.on('play-song')
def handlePlay(msg):
    print(msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketIo.run(app)
