from flask import Flask
from flask import render_template
from flask import request as freqs
import requests as reqs
import html

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sex():
	rez = "scrie numele cu virgula intre ele si dupa apasa pe buton"
	b = ""
	if freqs.method == "POST":
		b = freqs.form["nume"]
		lista = freqs.form["nume"].split(",")
		a = reqs.get("https://www.random.org/integers/", {"num" : 1, "min" : 1, "max" : len(lista), "col" : 1, "base" : 10, "format" : "plain", "rnd" : "new"}).text
		a = a[:-1]
		try:
			rez = lista[int(a)-1]
		except ValueError:
			rez = 'serverele <a href="http://random.org/">random.org</a> sunt ocupate acum, inceacra mai tarziu geiul;e'
	return render_template("index.html", rz = rez, inpt = b, unescape = html.unescape)

app.run(port=5000)