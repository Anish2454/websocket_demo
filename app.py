from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

@socketio.on('connected')
def handle_my_event(message):
    print "Socket Connected!"
    print str(message)

@socketio.on('msg')
def rec_msg(msg):
    print('***received message: ' + msg)
    print "***Modifying message..."
    msg += "12345"
    print "***New message: "
    print "***" + msg
    emit('response', msg)

if __name__ == '__main__':
    socketio.run(app)
