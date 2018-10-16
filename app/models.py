from app.main import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(80))
    message_author = db.Column(db.String(120))
