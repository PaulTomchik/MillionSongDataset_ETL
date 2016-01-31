#!/usr/bin/python

import os
import mat4py
import json

matDir = "/data/mat/"

# http://stackoverflow.com/a/16974952
for root, dirs, files in os.walk(matDir):
    path = root.split('/')
    for file in files:

        fBase, fExt = os.path.splitext(file)
        
        if (fExt == '.mat'):
            inF = os.path.normpath(root + '/' + file)
            data = mat4py.loadmat(inF)

            jsonDir = os.path.normpath('/data/json/' + "/".join(path[2:]) + '/')
            outF = fBase + ".json"
            outPath = os.path.normpath(jsonDir + outF)

            if not os.path.exists(jsonDir):
                os.makedirs(jsonDir)

            with open(outPath, "w") as outF:
                json.dump(data, outF)
