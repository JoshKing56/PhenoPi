import os
import yaml

def getExperimentList():
	explist = open("saved_experiments/experimentList.yml", "r")
	return(yaml.load(explist))	

def loadExperiment(experimentNumber):
        explist = getExperimentList()
        expfile = open("saved_experiments/" + explist[experimentNumber] + ".yml")
        return(yaml.load(expfile))

def addExperiment(savename, experimentData):
    filename = "saved_experiments/" + savename + ".yml"
    with open(filename, 'w+') as outfile:
        yaml.dump(experimentData, outfile, default_flow_style=False)
    explist = getExperimentList()
    print(explist)
    explist['first'] = explist['second']
    explist['second'] = explist['third']
    explist['third'] = savename
    print(explist)
    with open("saved_experiments/experimentList.yml", 'w+') as outfile:
        yaml.dump(explist, outfile, default_flow_style=False)
