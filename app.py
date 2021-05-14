from flask import Flask
from flask import render_template
from flask import request as freqs
from time import sleep
import requests as reqs
import html

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
	with open("nume.txt", "r") as f:
		nume = sorted(f.read().split(";"))
	win = None
	numealese = []
	if freqs.method == "POST":
		if freqs.form["aleg"] == "da":
			numealese = freqs.form.getlist("numealese")
			print(numealese)
			if len(numealese) <= 1:
				return render_template("newindex.html", nume = nume, unescape = html.unescape, numealese = numealese, noten = True, win = win)
			a = reqs.get("https://www.random.org/integers/", {"num" : 1, "min" : 0, "max" : len(numealese)-1, "col" : 1, "base" : 10, "format" : "plain", "rnd" : "new"}).text
			while not a[0].isdigit():
				a = reqs.get("https://www.random.org/integers/", {"num" : 1, "min" : 0, "max" : len(numealese)-1, "col" : 1, "base" : 10, "format" : "plain", "rnd" : "new"}).text
				sleep(1)
				print(a)
			a = int(a)
			win = numealese[a]
		elif freqs.form["aleg"] == "st":
			numealese = nume
		elif freqs.form["aleg"] == "dt":
			numealese = []
	return render_template("newindex.html", nume = nume, unescape = html.unescape, numealese = numealese, noten = False, win = win)

@app.route("/add", methods=["GET", "POST"])
def add():
	if freqs.method == "POST":
		with open("nume.txt", "a") as f:
			f.write(";" + freqs.form["nume"])
	return render_template("add.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
	with open("nume.txt", "r") as f:
		nume = sorted(f.read().split(";"))
	if freqs.method == "POST":
		numealese = freqs.form.getlist("numealese")
		nume = [i for i in nume if i not in numealese]
		with open("nume.txt", "w") as f:
			f.write(";".join(nume))
	return render_template("delete.html", nume = nume)

if __name__ == '__main__':
	app.run(port=5000, debug=True)