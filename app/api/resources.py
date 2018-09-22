from flask import Blueprint
from flask_restful import Api, Resource, url_for, reqparse, fields,marshal_with, abort
from app.models import Message
from app.main import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

resource_fields = {
    "id": fields.Integer,
    "message": fields.String,
    "message_author": fields.String
}

def get_message_or_404(id):
    message = Message.query.filter_by(id=id).first()
    if message is None:
        abort(404, message="Message {} doesn't exist".format(id))
    else:
        return message

class MessageList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        message_list = Message.query.all()
        return [message for message in message_list]

    @marshal_with(resource_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, help='Rate to charge for this resource', location="json")
        parser.add_argument('message_author', type=str, help='Rate to charge for this resource', location="json")
        args = parser.parse_args()
        new_message = Message(
            message = args["message"],
            message_author = args["message_author"]
        )

        db.session.add(new_message)
        db.session.commit()
        return new_message, 200

class MessageItem(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        message = get_message_or_404(id)
        return message


    @marshal_with(resource_fields)
    def put(self,id):
        message = get_message_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, help='Rate to charge for this resource', location="json")
        parser.add_argument('message_author', type=str, help='Rate to charge for this resource', location="json")
        args = parser.parse_args()
        if args["message"]:
            message.message = args["message"]
        if args["message_author"]:
            message.message_author = args["message_author"]
        db.session.commit()

        return message


    def delete(self,id):
        message = get_message_or_404(id)
        db.session.delete(message)
        db.session.commit()
        return {"Message":"Message deleted"}, 200

api.add_resource(MessageList, '/message')
api.add_resource(MessageItem, '/message/<int:id>')
