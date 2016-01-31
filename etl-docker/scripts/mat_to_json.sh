#!/usr/bin/env bash

python /etl/mat2jsonConverter.py

# http://stackoverflow.com/a/29584184
chown -R `stat -c "%u:%g" /data` /data
