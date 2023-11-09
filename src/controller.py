from src.app import app
from src.models import User, Message
from flask import render_template

@app.route('/', methods=["GET"])
def home():
   users = User.query.all()
   print(users)
   return render_template('home.html', users=users)

@app.route('/chat/<int:user_id>',  methods=["GET"])
def chat(user_id):
   user = User.query.get(user_id)
   messages = Message.query.filter_by(user_id=user_id).all()
   return render_template('chat.html', user=user, messages=messages)
