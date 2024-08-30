from flask import session
from flask_socketio import emit, join_room, leave_room
from app import socketio
from app.models import Message

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': session.get('username') + ' has entered the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    emit('status', {'msg': session.get('username') + ' has left the room.'}, room=room)

@socketio.on('message')
def on_message(data):
    room = data['room']
    username = session.get('username')
    message = data['message']
    Message.create(room, username, message)
    emit('message', {'username': username, 'message': message}, room=room)

@socketio.on('get_messages')
def get_messages(data):
    room = data['room']
    messages = Message.get_by_room(room)
    emit('load_messages', {'messages': list(messages)})