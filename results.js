var resultsViz = require('visualization-stream-mvr-results')
var IPCStream = require('electron-ipc-stream')
var ipcsR = new IPCStream('results')

var resultsStream = resultsViz.createStream()
ipcsR.pipe(resultsStream)

