#!/usr/bin/env bash

SUB_DIR=$1

python /PythonSrc/hdf5_to_matfile.py /data/hdf5/${SUB_DIR}

cd /data && for f in $(find "hdf5/${SUB_DIR}" -name '*.mat'); do
    m=$(echo $f | sed 's/hdf5/mat/g')
    mkdir -p $(dirname $m)
    mv $f $m
done

# http://stackoverflow.com/a/29584184
chown -R `stat -c "%u:%g" /data` /data
