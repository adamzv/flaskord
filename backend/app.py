from datetime import datetime
from flask import Flask, session, redirect, url_for, request, flash, render_template, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = "superbezpecnykluc"  # TODO generate proper secret key  #os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []
channels = ["default", ]
messages = [{"id": 0, "channel": channels[0], "message": "Test message", "author": "admin", "time": "18:41"},
            {"id": 1, "channel": channels[0], "message": "Test message", "author": "admin", "time": "19:11"}, ]


@app.route("/", methods=["GET", "POST"])
def index():
    if "username" in session:
        return render_template("index.html", channels=channels, user=session["username"])
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username in users:
            flash("Username is already taken.")
            return redirect(url_for("login"))
        else:
            session["username"] = username
            users.append(username)
            return redirect(url_for("index"))
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
    # TODO new socketio emit - delete oldest message
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
