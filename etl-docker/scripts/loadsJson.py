import os
import sys
import json
import time

#return a list, each element in this list is a dict().
# each dict() is a record of a song.
# the track_id should be the primary key.
def loadsJson(path):
    data = []
    with open(path) as f:
        for eachLine in f:
            data.append(json.loads(eachLine.rstrip()))
    return data

if __name__ == '__main__':
    data = loadsJson('./data_A.json')
    for item in data:
        print item