var io = require('socket.io-client'),
    socket = io.connect('http://localhost:8080');

socket.on('connect', function() {
  console.log('connected to server');
});

socket.on('go', function(){
  var fs = require('fs'),
      filename = 'data.txt';
  fs.readFile(filename, 'utf8', function(err, data) {
    if (err) {throw err;}
    console.log('sending data');
    socket.emit('sendDataToServer', {data: 'data'});
    socket.on('returnDataToClient',function(data) {
      console.log('data received:\n' + data);
    });
  });
});

