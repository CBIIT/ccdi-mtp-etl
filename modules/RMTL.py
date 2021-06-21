import logging.config
import modules.commons as commons
import json

logger = logging.getLogger(__name__)

def readRMTLCSV(path):
    return  commons.readCSVToDict(path)

def export(targetList,targetsFileName,path):
    # path correction
    if not path.endswith("/"):
        path = path + "/"
    commons.createDirectoryIfNotfound(path)

    #Save new target files
    with open(path+targetsFileName, mode="w") as outFile:
        for target in targetList:
            outFile.write(json.dumps(target, ensure_ascii=False) + "\n")
    logger.info("Save Processed Target file to %s", path+targetsFileName)

'''
Add rmtl propery to the target if match a record in the RMTL list

@:param 
    target    
    RMTLList
@:return target
'''
def addRMTLProperyToTarget(target,RMTLList):
     for rmtl in RMTLList:
         target["rmtl_fda_designation"]=""
         #  target id matchs Ensembl_ID
         if rmtl[0]==target["id"]:
             logger.info("target -- %s --- matches RMTL list %s ", target["id"], rmtl[2])
             target["rmtl_fda_designation"]=rmtl[2]
     return target


def process(targetPath,RMTLList,config):

    targetsFileName = targetPath.split("/")[-1]

    targetsWithRMTL = []

    logger.info("Parsing target file  %st", targetsFileName)
    targets = commons.readJsonWithMultipleObj(targetPath)

    #Add RMTL propery into targets
    for target in targets:
        targetsWithRMTL.append(addRMTLProperyToTarget(target,RMTLList))

    export(targetsWithRMTL,targetsFileName,config['output'])


'''
Validate configuration settings, make sure 
rmtl, targets and outputs fields are presents

@:returns  boolean [True | False]
    True   is vaild configuration settings
    False  something wrong with the configuration settings
'''
def isValid(config):
    if "inputs" in config \
            and "output" in config:
        return  True
    else:
        return False

'''
Run RMTL process

@:param
config
    rmtl:
      - data/inputs/rmtl.csv
    targets:
      - data/inputs/targets/part-00000-2099be1d-059f-4e90-9263-7d205e2ba50f-c000.json
    outputs:
    - data/outputs/targets/part-00000-2099be1d-059f-4e90-9263-7d205e2ba50f-c000.json
    
@:return  
    generate new json file that contains targets along with RMTL property.   
'''
def run(config):
    logger.info(config)
    if isValid(config):
        logger.info("read RMTL list from %s", config["inputs"]["rmtl"])
        # reads rmtl list
        RMTLDic=readRMTLCSV(config["inputs"]["rmtl"])

        # read targets
        for targetPath in config["inputs"]["targets"]:

            # process each target file with RMTL list
            process(targetPath,RMTLDic,config)

    else:
        logger.error("InValid Configuration setting for RMTL")

