# ppdc-data-pipeline
This repository contains scripts to process PPDC data.

## How to use this repo


```shell

python ./main.py  -c config.yaml

```

Main.py is the entry of the program and uses config.yaml file for the configuration settings. 

## Overview of config.yaml

The config.yaml file contains several sections. 

```shell
---
steps:
  - rmtl

rmtl:
  inputs:
    rmtl: data/inputs/rmtl.csv
    targets:
      - data/inputs/targets/part-00000-2099be1d-059f-4e90-9263-7d205e2ba50f-c000.json
  output: data/outputs/targets/
```

The config.yaml contains two sections:  

Steps: # ETL steps to execute

[step]: # configuration settings for a specific step.

