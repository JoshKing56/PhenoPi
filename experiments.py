import os
import yaml

def getExperimentList():
	explist = open("saved_experiments/experimentList.yml", "r")
	return(yaml.load(explist))	

def loadExperiment(experimentNumber):
        explist = getExperimentList()
        expfile = open("saved_experiments/" + explist[experimentNumber] + ".yml")
        return(yaml.load(expfile))

