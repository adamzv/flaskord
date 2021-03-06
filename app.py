from datetime import datetime
from flask import Flask, session, request, render_template, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os

app = Flask(__name__, static_url_path='')
CORS(app)
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV", "production")
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET", "Secret")
socketio = SocketIO(app)

users = []
channels = ["default", ]
messages = [{"id": 0, "channel": channels[0], "message": "Welcome!", "author": "admin", "time": "2019-03-10T13:44:26.205700"},]


@app.route("/", methods=["GET", "POST"])
def index():
    return app.send_static_file("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
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
    # Vue frontend will handle conversion to local time
    data["time"] = str(datetime.utcnow().isoformat())
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


if __name__ == "__main__":
    socketio.run(app)