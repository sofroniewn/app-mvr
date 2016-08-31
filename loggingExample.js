// check if 'session folder exists', if not make one
// look at most recent session number, and increment by one (if non-exist take 0)


// make directory with that name
// make directory inside called behaviour
// create fileName

// make file called session.data that gets appended to every data point
// make file called session.mazes that gets appended to every trial

    
// var path = './sessions/' + '000000' + '/behavior'
// mkdirp(path, function (err) {
//     if (err) console.error(err)
//     else console.log(path)
// });

// var path = './sessions/' + '000001' + '/behavior'
// mkdirp(path, function (err) {
//     if (err) console.error(err)
//     else console.log(path)
// });

var glob = require('glob')
var leftPad = require('left-pad')
var mkdirp = require('mkdirp')
var jsonfile = require('jsonfile')

// function createDir (number) {
//   var path = './sessions/' + leftPad(number, 6, 0) + '/behavior'
//   mkdirp(path, function (err) {
//       if (err) console.error(err)
//       else console.log(path)
//   })
// }

path = require('path')

// var number = null
// glob('./sessions/*', [], function (er, files) {
//   var used = []
//   files.forEach(function (el) {
//     used.push(Number(path.basename(el)))
//   })
//   console.log(used)
//   if (used.indexOf(number) === -1) {
//     if (used.length === 0) number = 0
//     else number = used[used.length-1]+1
//   }
//   console.log(number)
// })



// var mazeNames = []
// var mazes = []
// glob('./mazes/*.maze', [], function (er, files) {
//   files.forEach(function (el) {
//     var file = path.basename(el)
//     mazeNames.push(file)
//     jsonfile.readFile(el, function (err, obj) {
//       mazes.push(obj)
//       console.log(obj)
//     })
//   })
// })

// var dict = []; // create an empty array
// glob('./mazes/*.maze', [], function (er, files) {
//   files.forEach(function (el) {
//     jsonfile.readFile(el, function (err, obj) {
//       dict.push({
//         key: path.basename(el),
//         value: obj
//       })
//       console.log(dict)
//     })
//   })
// })

var mazes = {}; // create an empty array
glob('./mazes/*.maze', [], function (er, files) {
  files.forEach(function (el) {
    jsonfile.readFile(el, function (err, obj) {
      mazes[path.basename(el)] = obj
      console.log(mazes)
      console.log(Object.keys(mazes))
    })
  })
})

// dict.push({
//     key:   "keyName",
//     value: "the value"
// });



// return list of used numbers