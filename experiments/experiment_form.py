import os
import yaml

def getExperimentList():
	explist = open("experiments/saved_forms/experimentList.yml", "r")
	return(yaml.load(explist))	

def loadExperiment(experimentNumber):
        explist = getExperimentList()
        expfile = open("experiments/saved_forms/" + explist[experimentNumber] + ".yml")
        return(yaml.load(expfile))

def addExperiment(savename, experimentData):
    filename = "experiments/saved_forms/" + savename + ".yml"
    with open(filename, 'w+') as outfile:
        yaml.dump(experimentData, outfile, default_flow_style=False)
    explist = getExperimentList()
    print(explist)
    explist['first'] = explist['second']
    explist['second'] = explist['third']
    explist['third'] = savename
    print(explist)
    with open("experiments/saved_forms/experimentList.yml", 'w+') as outfile:
        yaml.dump(explist, outfile, default_flow_style=False)
