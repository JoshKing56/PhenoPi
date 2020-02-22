from flask import Flask, render_template, flash, request, redirect
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError
import os
from data_collection import assemble_data, camera_capture
from experiments import experiment_form

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

class MetaDataForm(Form):
        user = TextField("Username",[validators.Required("Please enter name")], default = " " )
        experiment = TextField("Experiment name/number", default = " ")
        species = TextField("Plant Species", default = " ")
        genotype = TextField("Plant Genotype", default = " ")
        plant = TextField("ID of the plant", default = " ")
        condition = TextField("Condition", default = " ")
        submit = SubmitField("Add Experiment")

class AddExpForm(MetaDataForm):
        savename = TextField("Name to save experiment by", default = " ")

@app.route("/", methods=['GET', 'POST'])
def index():
    print("Got here?")
    form = MetaDataForm()
    expList = experiment_form.getExperimentList() 
  	
    if request.method == "POST":
    	if "first" in request.form:
    		experimentData = experiment_form.loadExperiment("first")

    	elif "second" in request.form:
    		experimentData = experiment_form.loadExperiment("second")

    	elif "third" in request.form:
    		experimentData = experiment_form.loadExperiment("third")

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
        result = assemble_data.captureImage(metadata) 
        return render_template('success.html', succeded = result)

@app.route("/addexperiment", methods=['GET', 'POST'])
def addexp():
    form = AddExpForm()
    
    if request.method == "POST":
        experiment = {
                'User': request.form.get('user'),
                'Experiment Number': request.form.get('experiment'),
                'Plant Species': request.form.get('species'),
                'Plant Genotype': request.form.get('genotype'), 
                'Plant Number': request.form.get('plant'), 
                'Condition': request.form.get('condition') 
        }
        savename = request.form.get('savename')
        experiment_form.addExperiment(savename, experiment)
        expList = experiment_form.getExperimentList()
        return render_template('display.html', buttons = experiment_form.getExperimentList(), form = MetaDataForm())

    return render_template('addexperiment.html', form = form)

@app.route("/top_view", methods=['POST'])
def top_view():
    if request.method =="POST":
        print("Route triggered")
        camera_capture.preview_camera(15, 1)
    return ('', 204) # 204 means no content. This seems to be the only code that doesn't change the page
 

@app.route("/preview_side1", methods=['POST'])
def side_view1():
    if request.method =="POST":
        print("Route triggered")
        camera_capture.preview_camera(15, 2)
    return ('', 204)
 
@app.route("/preview_side2", methods=['POST'])
def side_view2():
    if request.method =="POST":
        print("Route triggered")
        camera_capture.preview_camera(15, 3)
    return ('', 204)
 

if __name__ == "__main__":
    app.run(debug=True)
