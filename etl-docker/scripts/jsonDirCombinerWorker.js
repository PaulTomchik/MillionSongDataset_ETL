#!/usr/bin/env node

"use strict"


let path = require('path')


module.exports = (dataDir, callback) => {
    "use strict";


    let fields = [
        'title', 
        'energy', 
        'loudness', 
        'tempo', 
        'artist_name', 
        'song_id',
        'track_id', 
        'key', 
        'year', 
    ];

    let fileCount = 0


    let walk = require('walk'),
        fs = require('fs'),
        walker

    walker = walk.walk(dataDir);

    let aggFilePath = path.join(path.dirname(dataDir), path.basename(dataDir) + '.json')


    let aggregationFileStream = fs.createWriteStream(aggFilePath) 

    let hotttnesssPattern = /hot+nes+/

    walker.on("file", function (root, fileStats, next) {

        let absPath = path.join(root, fileStats.name) 

        fs.readFile(absPath, function (err, data) {

            if (err) {
                console.error('\n====== Error reading ' + fileStats.name + '======')
                console.error(err.stack)
                console.error()
                return next()
            }

            try {
                
                let cleanedData = data.toString()
                cleanedData = cleanedData.replace(/NaN/g, '0')

                let songData = JSON.parse(cleanedData)


                let projectedData = fields.reduce((acc, field) => {

                    let value = (songData[field] !== undefined) ? songData[field] : null

                    acc[field] = value

                    return acc
                }, {})

                let hotttnesssKeys = Object.keys(songData).filter(k => k.match(hotttnesssPattern))

                for (let i = 0; i < hotttnesssKeys.length; ++i) {
                    let key = hotttnesssKeys[i].replace(hotttnesssPattern, "hotttnesss")
                    projectedData[key] = songData[hotttnesssKeys[i]]
                }

                ++fileCount
                
                //console.log(projectedData)
                aggregationFileStream.write(JSON.stringify(projectedData) + '\n')

            } catch (e) {
                console.error('\n------ Error working with ' + absPath + '\'s data. ------')
                //console.log(data)
                console.error(e.stack)
                console.error()
            } finally {
                return next();
            }
        });
    });

    walker.on("errors", function (root, nodeStatsArray, next) {
        console.error('\n>>>>>> Encountered error: ');
        console.error(require('util').inspect(nodeStatsArray))
        console.error()

        next();
    });

    walker.on("end", function () {
        callback(null, dataDir.split('/').slice(-1) + '--' + fileCount)
    });


}
