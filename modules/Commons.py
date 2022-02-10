import logging.config
import csv
import json
import os
import sys

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
    return jsonList


# (source): https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total, status=''):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
