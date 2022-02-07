import logging.config
import modules.Commons as commons
import json

logger = logging.getLogger(__name__)


def export(optionList, dataFileName, path):
    # path correction
    if not path.endswith("/"):
        path = path + "/"
    commons.createDirectoryIfNotfound(path)

    # Save new data files
    with open(path+dataFileName, mode="w") as outFile:
        outFile.write("[\n")
        i = 1
        for option in optionList:
            outFile.write("\t"+json.dumps(
                option, ensure_ascii=False))
            if i != len(optionList):
                outFile.write(",\n")
            i += 1
        outFile.write("\n]")
    logger.info("Save Processed (Disease or Target) Options to %s",
                path+dataFileName)


def process(dataPath, config):
    dataFileName = dataPath.split("/")[-1]
    targetFileName = "targetOptions.json"
    diseaseFileName = "diseaseOptions.json"

    aggregateTarget = []
    targetOptions = []
    aggregateDisease = []
    diseaseOptions = []

    logger.info("Parsing Pediatric Cancer Data Navigation file %s to "
                "return list of Disease and Target options", dataFileName)
    data = commons.readJsonWithMultipleObj(dataPath)
    counter = 0
    datalength = len(data[0])
    # Add Target and Disease property into list of options
    for row in data[0]:
        diseaseId = row["diseaseFromSourceMappedId"]
        targetId = row["targetFromSourceId"]
        if aggregateDisease.count(diseaseId) == 0:
            aggregateDisease.append(diseaseId)
            diseaseOptions.append(
                {"Disease": row["Disease"], "diseaseFromSourceMappedId": diseaseId})

        if aggregateTarget.count(targetId) == 0:
            aggregateTarget.append(targetId)
            targetOptions.append(
                {"Gene_symbol": row["Gene_symbol"], "targetFromSourceId": targetId})

        counter += 1
        commons.progress(counter, datalength)

    # Sort by Disease name
    logger.info("Sorting Disease Options by Disease value")
    diseaseOptions = sorted(diseaseOptions, key=lambda d: d["Disease"].lower())
    logger.info("Sorting Target Options by Gene_symbol value")
    # Sort by Gene symbol
    targetOptions = sorted(
        targetOptions, key=lambda d: d['Gene_symbol'].lower())

    export(diseaseOptions, diseaseFileName, config['output'])
    export(targetOptions, targetFileName, config['output'])


'''
Validate configuration settings, make sure
input data and outputs fields are presents

@:returns  boolean [True | False]
    True   is vaild configuration settings
    False  something wrong with the configuration settings
'''


def isValid(config):
    if "inputs" in config \
            and "output" in config:
        return True
    else:
        return False


'''
Run ped-can-data-nav process

@:param
config
    rmtl: 
      ...
    ped-can-data-nav:
      inputs:
        rmtl: data/inputs/rmtl.csv
        navigation:
          - /Users/tesfatsionnh/Documents/Work/Data/chopDataNavigationTable.json

      output: data/outputs/navigation/

@:return
    generate two new json file that contains unique list of target and disease. 
    The list will be consumed as selection option for searching purpose.
'''


def run(config):
    logger.info(config)
    if isValid(config):
        logger.info("read ped-can-data-nav from %s",
                    config["inputs"]["navigation"])
        # read data for Pediatric Cancer Data Navigation
        for navigationPath in config["inputs"]["navigation"]:
            # process each data file
            process(navigationPath, config)

    else:
        logger.error("InValid Configuration setting for ped-can-data-na")
