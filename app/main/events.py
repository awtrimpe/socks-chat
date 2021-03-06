from flask import request, session
from flask_socketio import emit, join_room, leave_room

from app import socketio
from app.main.routes import authenticated_only


@socketio.on('joined', namespace='/chat')
@authenticated_only
def joined(message):
    '''Sent by clients when they enter a room.
    A status message is broadcast to all people in the room.'''
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
@authenticated_only
def text(message):
    '''Sent by a client when the user entered a new message.
    The message is sent to all people in the room.'''
    room = session.get('room')
    emit('message', {'msg': message['msg'],
                     'name': session.get('name'),
                     'id': request.sid}, room=room)


@socketio.on('left', namespace='/chat')
@authenticated_only
def left(message):
    '''Sent by clients when they leave a room.
    A status message is broadcast to all people in the room.'''
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') +
                    ' has left the room.'}, room=room)


@socketio.on('typing', namespace='/chat')
@authenticated_only
def typing(message):
    '''Sent by a client when the user is typing. A status message is broadcast to
    all people in the room'''
    room = session.get('room')
    emit('user_typing', {'name': session.get(
        'name'), 'id': request.sid}, room=room)
