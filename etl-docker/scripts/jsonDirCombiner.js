#!/usr/bin/env node

"use strict"

// This script gets the Subdirectories of the json directory, then 
// spawns workers that build the per directory arrays of song/objects.

let fs = require('fs')
let path = require('path')

let dataDir = '/data/json/'

let workerFarm = require('worker-farm'),
    workers    = workerFarm(require.resolve('./jsonDirCombinerWorker'))

let subdirs = fs.readdirSync(dataDir)
                .map(file => path.join(dataDir, file))
                .filter(absPath => fs.statSync(absPath).isDirectory())


let subDirsCount = subdirs.length
let subDirsDone  = 0

for (let i = 0; i < subdirs.length; ++i) {
    workers(subdirs[i], function (err, outp) {
        
        console.log(outp);

        if (++subDirsDone === subDirsCount) {
            workerFarm.end(workers)
        }
    }) 
}
