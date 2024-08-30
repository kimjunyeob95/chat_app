from flask import render_template, request, redirect, url_for, session
from app import app
from app.models import User, ChatRoom

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = User.find_by_username(username)
        if not user:
            User.create(username)
        session['username'] = username
        return redirect(url_for('chat_rooms'))
    return render_template('login.html')

@app.route('/chat_rooms')
def chat_rooms():
    if 'username' not in session:
        return redirect(url_for('login'))
    rooms = ChatRoom.get_all()
    return render_template('chat_rooms.html', rooms=rooms)

@app.route('/chat/<room_name>')
def chat(room_name):
    if 'username' not in session:
        return redirect(url_for('login'))
    room = ChatRoom.find_by_name(room_name)
    if not room:
        room = ChatRoom.create(room_name)
    return render_template('chat.html', room=room, username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))