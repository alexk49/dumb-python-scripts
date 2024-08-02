import sqlite3

from bottle import route, run, template, static_file


@route("/static/<filename:path>")
def server_static(filename):
    return static_file(filename, root="static")


@route("/picnic")
def show_picnic():
    db = sqlite3.connect("picnic.db")
    c = db.cursor()
    c.execute("SELECT item,quant FROM picnic")
    data = c.fetchall()
    c.close()
    output = template("bring_to_picnic", rows=data)
    return output


@route("/")
def home():
    return "Hello World!"


@route("/hello")
def hello():
    return "Hello again!"


run(host="localhost", port=8080, debug=True, reloader=True)
