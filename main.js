var electron = require('electron')
var ipcMain = require('electron').ipcMain
var IPCStream = require('electron-ipc-stream')
var glob = require('glob')
var path = require('path')
var leftPad = require('left-pad')
var mkdirp = require('mkdirp')
var jsonfile = require('jsonfile')
var protoBuf = require('protocol-buffers')

var app = electron.app
var BrowserWindow = electron.BrowserWindow

var controlWindow = null
function createControlWindow() {
  controlWindow = new BrowserWindow({
    width: 600,
    height: 300,
    x: 0,
    y: 0
  })
  controlWindow.loadURL(`file://${__dirname}/control.html`)

  controlWindow.on('closed', function () {
    controlWindow = null
  })
}

var mazeVizWindow = null
function createMazeVizWindow() {
  mazeVizWindow = new BrowserWindow({
    width: 600,
    height: 800,
    resizable: false,
    frame: false,
    x: 600,
    y: 0
  })
  mazeVizWindow.loadURL(`file://${__dirname}/mazeViz.html`)
  mazeVizWindow.on('closed', function () {
    mazeVizWindow = null
  })
}

var resultsWindow = null
function createResultsWindow() {
  resultsWindow = new BrowserWindow({
    width: 600,
    height: 600,
    x: 0,
    y: 300
  })
  resultsWindow.loadURL(`file://${__dirname}/results.html`)

  resultsWindow.on('closed', function () {
    resultsWindow = null
  })
}

/////////////////////////////////////////////////////////////////


// var player = {
//   playerStart: [0, 5],
//   playerShape: [
//     [-2,-1.5], [0, 1.5], [2, -1.5]
//   ],
// }

var mazes = {}; // create an empty array
glob('./mazes/*.maze', [], function (er, files) {
  files.forEach(function (el) {
    jsonfile.readFile(el, function (err, obj) {
      mazes[obj[0].name] = obj[0]
    })
  })
})

////////////////////////////////////////////////////////////
var experiment = require('experiment-stream-mvr-map')()
var device = require('device-stream-mvr-stdin')()
var logging = require('time-stream')
var fs = require('fs')
var encoderResults = protoBuf(fs.readFileSync('./proto/behavior.proto'))
var encoderMaze = protoBuf(fs.readFileSync('./proto/maze.proto'))

app.on('ready', function() {
  createResultsWindow()
  createControlWindow()
  createMazeVizWindow()

  var loggingFlag = false
  var resetFlag = true
  var sessionNumber = 0

  var ipcsD = new IPCStream('device', mazeVizWindow)
  var ipcsT = new IPCStream('trial', mazeVizWindow)
  var ipcsR = new IPCStream('results', resultsWindow)

  var deviceStream = device.createStream()
  var exptStream = experiment.createStream()
  
  var resultStream = deviceStream.pipe(exptStream)
  var loggingDataStream = null
  var loggingMazeStream = null
  //resultStream.pipe(deviceStream)
  resultStream.pipe(ipcsD)
  resultStream.pipe(ipcsR)
  experiment.trialStream.pipe(ipcsT)

  controlWindow.webContents.on('did-finish-load', function () {
    controlWindow.webContents.send('initList', Object.keys(mazes))
    controlWindow.webContents.send('initOrder', [0, 1, 0])
  })

  ipcMain.on('reset', function () {
    console.log('reset')
    resetFlag = true
  })

  ipcMain.on('initTrial', function (event, key) {
    console.log(mazes[key])
    experiment.initTrial(mazes[key])
  })

  ipcMain.on('play', function () {
    console.log('play', loggingFlag, resetFlag)
    if (loggingFlag & resetFlag) {
      // make directories
      console.log('start logs')
      savePath = './sessions/' + leftPad(sessionNumber, 6, 0) + '/behavior'
      mkdirp(savePath)
      if (loggingDataStream !== null) resultStream.unpipe(loggingDataStream)
      loggingDataStream = logging.createWriteStream(savePath + '/behavior.data', encoderResults.Data)
      resultStream.pipe(loggingDataStream)
      //if (loggingMazeStream !== null) experiment.trialStream.unpipe(loggingMazeStream)
      //loggingMazeStream = logging.createWriteStream(savePath + '/session.maze', encoderMaze.Data)
      //experiment.trialStream.pipe(loggingMazeStream)
    }
    device.start()
  })

  ipcMain.on('pause', function () {
    console.log('pause')
    resetFlag = false 
    device.stop()
  })

  ipcMain.on('advance', function () {
    console.log('advance')
    experiment.advanceTrial()
  })

  ipcMain.on('nextTrial', function (event, key) {
    experiment.updateTrial(mazes[key])
  })

  ipcMain.on('logging', function (event, data) {
    console.log('logging', data)
    loggingFlag = data
  })

  ipcMain.on('number', function (event, data) {
    console.log('number', data)
    sessionNumber = Number(data)
    glob('./sessions/*', [], function (er, files) {
      var used = []
      files.forEach(function (el) {
        used.push(Number(path.basename(el)))
      })
      if (sessionNumber < 0) sessionNumber = 0
      if (used.indexOf(sessionNumber) !== -1) {
        sessionNumber = used[used.length-1]+1
      }
      controlWindow.webContents.send('number', sessionNumber)
    })
  })

  experiment.trialStream.on('data', function (data) {
    if (!data.init) controlWindow.webContents.send('nextTrial', data.map.name)
  })

  mazeVizWindow.on('close', function () {
    ipcsD.pause()
    ipcsT.pause()
    resultStream.pause()
    deviceStream.pause()
  })
})

process.stdin.on('data', function(data) {
  if (data.toString().trim() === 'q') app.quit()
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  if (controlWindow === null) {
    createControlWindow()
  }
  if (mazeVizWindow === null) {
    createMazeVizWindow()
  }
  if (resultsWindow === null) {
    resultsWindow()
  }
})