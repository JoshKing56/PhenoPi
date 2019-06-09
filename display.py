from flask import Flask, render_template, flash, request, redirect
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError
import os
import camera

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

class MetaDataForm(Form):
    user = TextField("User name",[validators.Required("Please enter name")], default="Josh") 
    species = TextField("Species of plant", default = "Barley")
    plant = TextField("ID of the plant", default = "1")
    experiment = TextField("Experiment name/number", default = "PhenoPi rig testing")
    submit = SubmitField("Capture picture")

@app.route("/")
def index():
    form = MetaDataForm()
    return render_template('display.html', user = "User", form = form)

@app.route("/picture", methods=['GET', 'POST'])
def takePicture():
    if request.method =="POST":
        metadata = {'User': request.form.get('user'), "Plant species": request.form.get('species'), "Plant Number": request.form.get('plant'), "Experiment Number": request.form.get('experiment')}
        result = camera.captureImage(metadata) 
        return render_template('success.html', succeded = result)


if __name__ == "__main__":
    app.run(debug=True)
