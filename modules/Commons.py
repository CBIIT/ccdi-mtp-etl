import logging.config
import csv
import json
import os

logger = logging.getLogger(__name__)

def readCSVToDict(path):
        with open(path, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)


def createDirectoryIfNotfound(path):
    if not os.path.exists(path):
        os.makedirs(path)

def readJsonWithMultipleObj(path):
    jsonList = []
    with open(path) as f:
        for jsonObj in f:
            jsonList.append(json.loads(jsonObj))
    return  jsonList