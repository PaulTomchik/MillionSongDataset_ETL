#!/usr/bin/env bash

python /PythonSrc/hdf5_to_matfile.py /data/hdf5

cd /data && for f in $(find hdf5/ -name '*.mat'); do
    m=$(echo $f | sed 's/hdf5/mat/g')
    mkdir -p $(dirname $m)
    mv $f $m
done

chown -R `stat -c "%u:%g" /data` /data
