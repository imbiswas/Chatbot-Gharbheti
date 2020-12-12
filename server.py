from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import handler
import time

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'nuttertools'
socketio = SocketIO(app, ping_timeout=30, logger=False, engineio_logger=False)

#routes to the home
@app.route('/')
@app.route('/gharbheti/chat')
def chat():
  return render_template('index.html')

@socketio.on('message', namespace='/chat')

#fetch message from the browser
def chat_message_receive(message):
  # emit('typing',{'data':{'message':'typing','author':'Ghar Bheti'}}, broadcast=False)
  # print("message = ", message)
  # emit('message', {'data': message['data']}, broadcast=False)

  user_message= message['data']['message']
  user_id=message['data']['id']
  name=message['data']['author']
  email=message['data']['email']
  contact=message['data']['contact']
  
  time.sleep(1)
  sender = handler.chat(user_message,user_id,name,email,contact)
  receiver=sender.result()

  #send response message to the browser
  emit('message',{'data':{'message':receiver,'author':'Ample Cube'}}, broadcast=False)

@socketio.on('connect', namespace='/chat')
def test_connect():
  emit('my response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0')
