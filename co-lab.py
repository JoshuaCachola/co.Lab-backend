from app import app
from flask_socketio import SocketIO, send, join_room, leave_room
import os

ROOMS = set('cacholaj')
socketIo = SocketIO(app, cors_allowed_origins='*')


@socketIo.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(f'{username} has entered the room.', room=room)


@socketIo.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(f'{username} has left the room', room=room)


@socketIo.on('new_room')
def new_room(data):
    ROOMS.add(data['new_room_name'])
    room = data['new_room_name']
    username = data['username']
    join_room(data['new_room_name'])
    send({"msg": f'{username} has created the a room'}, room=room)


# @socketIo.on('close_room')
# def close_room(data):
#     ROOMS.remove(data['remove_room'])

# @socketIo.on('message')
# def handleMessage(msg):
#     print(msg)
#     send(msg, broadcast=True)
# @socketIo.on('play-song')
# def handlePlay(msg):
#     print(msg)
#     send(msg, broadcast=True)


if __name__ == '__main__':
    socketIo.run(app)
