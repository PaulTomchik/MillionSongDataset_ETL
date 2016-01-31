Docker is a hard dependency.

Put the data.tar.gz file in the project root.

You can get it here: https://drive.google.com/folderview?id=0Bx8HvafDsU2cazRGdUtlYjVJekk&usp=sharing

The scripts should be called in the following order:

   + `./bin/getMSongsDB.sh`
   + `./bin/inflateTheDataTar.sh`
   + `./bin/buildTheDockerImage.sh`
   + `./bin/toMatfile.sh`
   + `./bin/toJSON.sh`

Note: the last two scripts should each take >10 minutes to complete.

