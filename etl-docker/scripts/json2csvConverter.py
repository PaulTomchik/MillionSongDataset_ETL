#!/usr/bin/env python

import os
import re
import csv
import json
import mat4py



# Based on code found here: http://stackoverflow.com/a/1872081
#                           http://stackoverflow.com/a/16974952


TARGET_DIR = "../../data/json/"

csvDir = '../../data/projections/'
csvFileName = 'data_A.csv'

fields = [
    'artist_hotttnesss', 
    'title', 
    'energy', 
    'loudness', 
    'tempo', 
    'artist_name', 
    'track_id', 
    'key', 
    'year', 
    'song_hotttnesss'
]


def convert_JSON_to_CSV ():


    csvFilePath = os.path.join(csvDir, csvFileName)

    csvWriter = csv.writer(open(csvFilePath, 'w'))

    csvWriter.writerow(fields)



    for jsonDir, dirs, files in os.walk(TARGET_DIR):

        for fileName in files:

            fileNameBase, fileNameExtension = os.path.splitext(fileName)
            
            if (fileNameExtension == '.json'):

                jsonFilePath  = os.path.join(jsonDir, fileName)
                print '>>>', jsonFilePath

                with open(jsonFilePath) as jsonFile:
                    data = json.loads(jsonFile.read())
                    csvWriter.writerow([unicode(data[field]).encode("utf-8") for field in fields])

if __name__ == '__main__':
    convert_JSON_to_CSV()
