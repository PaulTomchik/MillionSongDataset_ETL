Docker is a hard dependency.

Put the data.tar.gz file in the project root.

You can get it here: https://drive.google.com/folderview?id=0Bx8HvafDsU2cazRGdUtlYjVJekk&usp=sharing
For the entire dataset: https://www.opensciencedatacloud.org/publicdata/million-song-dataset/

The scripts should be called in the following order:

   + `./bin/getMSongsDB.sh`
   + `./bin/inflateTheDataTar.sh`
   + `./bin/buildTheDockerImage.sh`
   + `./bin/toMatfile.sh`
   + `./bin/toJSON.sh`

Note: the last two scripts should each take >10 minutes to complete.


#========================================================================
Houston, we have a problem....

It (hdf5 -> .mat) converter throws if the input file is not good.
Apparently, after ~500K songs, the transformations stopped.
To reach that point took 11 hours.

So, at this point the plan is to work with those 500K songs.
Then,
	It looks like some directories were completely ignored.
	These can be transformed as is.

	The directory where errors occur will need to be handled differently.

		For all already transformed files, mark their file name and ignore.
			This will entail iterating over the .mat files dir and marking those files.
			Then we iterate over the hdf5 files and transform the unmarked.
			The key will be identifying the borked files.
				Not sure how to do that yet.

	HDF5 subdirectories yet to transform: [B, E, G, K, N, O, P, T, V, X, Y]	
