from datetime import datetime
from flask import Flask, session, request, render_template, jsonify, send_file, current_app
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV", "production")
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET", "Secret")
socketio = SocketIO(app)

users = []
channels = ["default", ]
messages = [{"id": 0, "channel": channels[0], "message": "Test message", "author": "admin", "time": "18:41"},
            {"id": 1, "channel": channels[0], "message": "Test message", "author": "admin", "time": "19:11"}, ]

APP_DIR = os.path.dirname(__file__)
DIST_DIR = os.path.join(APP_DIR, 'dist')


@app.route("/", methods=["GET", "POST"])
def index():
    dist_path = os.path.join(DIST_DIR, "index.html")
    print(DIST_DIR)
    print(dist_path)
    return send_file(dist_path)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #username = request.form.get("username")
        username = request.get_json(silent=True).get("username")
        print(username)
        if username in users:
            """
            flash("Username is already taken.")
            return redirect(url_for("login"))
            """
            return jsonify(status="Username is already taken.")
        else:
            session["username"] = username
            users.append(username)
            # return redirect(url_for("index"))
            return jsonify(status="ok", username=username)
    return render_template("login.html")


@app.route("/<channel>")
def get_channel(channel):
    if channel in channels:
        mes = []
        for i in range(0, len(messages)):
            if channel == messages[i]["channel"]:
                mes.append(messages[i])
        print(mes)
        return jsonify(messages=mes)
    else:
        return jsonify(messages=[])


@app.route("/channels")
def get_channels():
    return jsonify(channels=channels)


@socketio.on("send msg")
def msg(data):
    msg_id = messages[-1]["id"]
    msg_id += 1

    data["time"] = str(datetime.now())[11:16]
    data["id"] = msg_id
    messages.append(data)
    check_messages_limit(data.get("channel"))
    emit("newMessage", data, broadcast=True)


@socketio.on("create channel")
def channel(data):
    chnnl = data["channel"]
    if chnnl not in channels:
        channels.append(chnnl)
        emit("newChannel", data, broadcast=True)


def check_messages_limit(channel):
    temp_messages = list(filter(lambda x: x.get("channel") == channel, messages))
    if len(temp_messages) > 100:
        # only 100 messages per channel are allowed, next function removes the oldest message from channel
        next(messages.remove(x) for x in messages if x.get("channel") == channel)
