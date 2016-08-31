var viz = require('visualization-stream-mvr-map')()
var IPCStream = require('electron-ipc-stream')
var ipcsD = new IPCStream('device')
var ipcsT = new IPCStream('trial')
var ipcRenderer = require('electron').ipcRenderer

var stream = null
var waiting = true
ipcsT.on('data', function (data) {
  if (waiting) {
    stream = viz.createStream(data.maze)
    ipcsD.pipe(stream)
  } else {
    viz.updateTrial(data.maze)
    waiting = false
  }
})


