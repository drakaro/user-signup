from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def signup():
    template = jinja_env.get.template('name_here.html')
    return template.render()


app.run()