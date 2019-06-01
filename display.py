from flask import Flask, render_template, flash, request, redirect
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError
import os
# import camera

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

class MetaDataForm(Form):
    user = TextField("User name",[validators.Required("Please enter name")], default="Josh") 
    species = TextField("Species of plant", default = "Barley")
    plant = TextField("ID of the plant", default = "1")
    experiment = TextField("Experiment name/number", default = "PhenoPi rig testing")
    submit = SubmitField("Capture picture")

@app.route("/", methods=['GET', 'POST'])
def index():
    form = MetaDataForm()
    name = ""
    if request.method =="POST":
        metadata = {'User': form.user.data, "Plant species": form.species.data, "Plant Number": form.plant.data}
        result = camera.captureImage(metadata) #TODO: Make a trycatch here
    return render_template('display.html', form = form)

@app.route("/picture")
def takePicture():
    return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
