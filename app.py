from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route("/")
def prompt_fill_in():
    fill_ins = story.prompts
    return render_template("prompts.html", fill_in_prompts=fill_ins)

@app.route("/madlib")
def render_madlib():
    madlib = story.generate(request.args)
    return render_template("madlib.html", story=madlib)