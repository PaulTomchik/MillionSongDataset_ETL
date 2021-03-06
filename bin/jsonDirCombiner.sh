#!/usr/bin/env bash

###############################################################################
# The following was taken directly from http://stackoverflow.com/a/246128
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
################################################################################

docker run -v "${DIR}/../data/:/data" \
           -v "${DIR}/../etl-docker/scripts/:/etl" \
           node:5.10 bash -c "node /etl/jsonDirCombiner.js"

