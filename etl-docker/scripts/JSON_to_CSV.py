#!/usr/bin/env python

import os
import csv
import json

# Based on code found here: http://stackoverflow.com/a/1872081

# For running on the host.
PATH_TO_DIR = '../../data/projections/data_A/'

# For using the docker container.
# PATH_TO_DIR = '/data/projections/data_A'

def convert_JSON_to_CSV ():

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

    inFilePath  = os.path.join(PATH_TO_DIR, 'data_A.json')
    outFilePath = os.path.join(PATH_TO_DIR, 'data_A.csv')

    csvWriter = csv.writer(open(outFilePath, 'w'))

    csvWriter.writerow(fields)

    with open(inFilePath) as inFile:
        for jsonRow in inFile:
            data = json.loads(jsonRow)
            csvWriter.writerow([unicode(data[field]).encode("utf-8") for field in fields])


if __name__ == '__main__':
    convert_JSON_to_CSV()
