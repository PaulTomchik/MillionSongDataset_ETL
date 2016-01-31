#!/usr/bin/python

import os
import re
import json
import mat4py


TARGET_DIR = "/data/mat/"


# http://stackoverflow.com/a/16974952
for matDir, dirs, files in os.walk(TARGET_DIR):

    for fileName in files:

        jsonDir = re.sub('/mat/', '/json/', matDir)

        fileNameBase, fileNameExtension = os.path.splitext(fileName)
        
        if (fileNameExtension == '.mat'):

            inFilePath  = os.path.join(matDir, fileName)
            outFilePath = os.path.join(jsonDir, fileNameBase + '.json')

            data = mat4py.loadmat(inFilePath)

            if not os.path.exists(jsonDir):
                os.makedirs(jsonDir)

            with open(outFilePath, "w") as outFile:
                json.dump(data, outFile)
