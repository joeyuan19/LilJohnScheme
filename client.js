var io = require('socket.io-client'),
    socket = io.connect('http://localhost:8080');

socket.on('go', function(){
  console.log('it worked!');
});

