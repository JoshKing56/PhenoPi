from flask import Flask, render_template, flash, request, redirect
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError
import os
import camera
import experiments 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

class MetaDataForm(Form):
        user = TextField("Username",[validators.Required("Please enter name")], default = " " )
        experiment = TextField("Experiment name/number", default = " ")
        species = TextField("Plant Species", default = " ")
        genotype = TextField("Plant Genotype", default = " ")
        plant = TextField("ID of the plant", default = " ")
        condition = TextField("Condition", default = " ")
        submit = SubmitField("Capture picture")

@app.route("/", methods=['GET', 'POST'])
def index():
	form = MetaDataForm()
	expList = experiments.getExperimentList() 
  	
	if request.method == "POST":
		if "first" in request.form:
			experimentData = experiments.loadExperiment("first")

		elif "second" in request.form:
			experimentData = experiments.loadExperiment("second")

		elif "third" in request.form:
			experimentData = experiments.loadExperiment("third")

		form.user.data = experimentData["User"]
		form.experiment.data = experimentData["Experiment Number"]
		form.species.data = experimentData["Plant Species"]
		form.genotype.data = experimentData['Plant Genotype']
		form.plant.data = experimentData['Plant Number']
		form.condition.data = experimentData['Condition']
		return render_template('display.html', buttons = expList, form = form)
		
	return render_template('display.html', buttons = expList, form = form)

@app.route("/picture", methods=['GET', 'POST'])
def takePicture():
     if request.method =="POST":
        metadata = {
                'User': request.form.get('user'),
                'Experiment Number': request.form.get('experiment'),
                'Plant Species': request.form.get('species'),
                'Plant Genotype': request.form.get('genotype'), 
                'Plant Number': request.form.get('plant'), 
                'Condition': request.form.get('condition') 
        }
        result = camera.captureImage(metadata) 
        return render_template('success.html', succeded = result)


if __name__ == "__main__":
    app.run(debug=True)
