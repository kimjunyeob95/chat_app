from app import mongo
from datetime import datetime

class User:
    @staticmethod
    def create(username):
        return mongo.db.users.insert_one({'username': username, 'created_at': datetime.utcnow()})

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

class ChatRoom:
    @staticmethod
    def create(name):
        return mongo.db.chat_rooms.insert_one({'name': name, 'created_at': datetime.utcnow()})

    @staticmethod
    def get_all():
        return mongo.db.chat_rooms.find()

    @staticmethod
    def find_by_name(name):
        return mongo.db.chat_rooms.find_one({'name': name})

class Message:
    @staticmethod
    def create(room_id, username, content):
        return mongo.db.messages.insert_one({
            'room_id': room_id,
            'username': username,
            'content': content,
            'created_at': datetime.utcnow()
        })

    @staticmethod
    def get_by_room(room_id, limit=50):
        return mongo.db.messages.find({'room_id': room_id}).sort('created_at', -1).limit(limit)