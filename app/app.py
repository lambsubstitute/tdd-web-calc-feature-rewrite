from lib2to3.pgen2.token import EQUAL
from multiprocessing.pool import INIT
from unittest import case
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
from threading import Lock

import calculator

async_mode = None
app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecretsalt"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode=async_mode)
thread = None
thread_lock = Lock()

# COMMAND CONSTANTS
commands = {
    "INIT": "intialise",
    "CLEAR": "clear",
    "SIGN": "sign",
    "PERCENT": "%",
    "DIVIDE": "/",
    "MULTIPLY": "*",
    "SUBTRACT": "-",
    "ADD": "+",
    "EQUALS": "=",
    "NINE": "9",
    "EIGHT": "8",
    "SEVEN": "7",
    "SIX": "6",
    "FIVE": "5",
    "FOUR": "4",
    "THREE": "3",
    "TWO": "2",
    "ONE": "1",
    "ZERO": "0",
}


@app.route("/")
def index():
    return render_template("index.html", sync_mode=socketio.async_mode)


@socketio.on("command")
def command(command):
    print(f"Received command: {command}")

    # TODO: Implement clear

    # INIT
    if command["command"] == commands["INIT"]:
        session["calculator"] = calculator.Calculator()
        session["calculation"] = []
        send(session["calculator"].value, "")
        return

    calc = session["calculator"]
    calculation = session["calculation"]

    # Interpret commands on every button press
    calculation.append(command["command"])

    # Parse when Equals if pressed
    if command["command"] == commands["EQUALS"]:
        print(f"Calculating answer for: {calculation}")
        try:
            calc.parse(calculation)
            send(calc.value, " ".join([str(x) for x in calc.calculation]))
            session["calculation"] = []
        except Exception as e:
            send(calc.value, "", error=str(e))
            print(str(e))
            session["calculation"] = []
            return


### Helper functions
def send(value, calculation, error=None):
    if error is None:
        emit("response", {"value": value, "calculation": calculation})
    else:
        emit("response", {"value": value, "calculation": calculation, "error": error})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
