import os
from datetime import datetime
from flask import Flask, session, redirect, url_for, request, flash, render_template, jsonify
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "superbezpecnysecrét"  #os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []
channels = ["default", ]
messages = [{"channel": channels[0], "message": "Test message", "author": "admin", "time": "18:41"},
            {"channel": channels[0], "message": "Test message", "author": "admin", "time": "19:11"}, ]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    if request.method == "POST":
        channel = request.form.get("channel")
        if channel in channels:
            flash("Channel already exists!")
            redirect(url_for("index"))
        else:
            channels.append(channel)
    """
    if "username" in session:
        print("INdex")
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
        return jsonify(messages=mes)
    else:
        return jsonify(messages=[])


@socketio.on("send msg")
def msg(data):
    msg = data

    msg["time"] = str(datetime.now())[11:16]
    global messages
    messages.append(msg)
    emit("new message", msg, broadcast=True)


@socketio.on("create channel")
def channel(data):
    chnnl = data["channel"]
    global channels
    if chnnl not in channels:
        print(channels)
        channels.append(chnnl)
        print(channels, 2)
        emit("new channel", data, broadcast=True)

