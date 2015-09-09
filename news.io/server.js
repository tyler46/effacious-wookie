var fs = require('fs')
  , http = require('http')
  , socketio = require('socket.io')
  , redis = require('redis')
  , querystring = require('querystring');

var sub = redis.createClient(6379, 'localhost');

sub.subscribe('news');

var handleRequest = function (req, res) {

  fs.readFile('./index.html', function (err, data) {
    res.writeHead(200);
    res.write(data);
    res.end();
  });
};

server = http.createServer(handleRequest);

var io = socketio(server);

io.on('connection', function (socket) {
  console.log('got connected');

  // Client creates a new article via socket.io
  socket.on('new article', function (data) {
    console.log(data);
    payload = querystring.stringify({
      reporter: data.reporter,
      headline: data.headline
    });


    var options = {
      host: '0.0.0.0',
      port: 8000,
      path: '/ws/article/',
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': payload.length
      }
    };

    // Send request to Django
    var req = http.request(options, function (res) {
      console.log('STATUS: ' + res.statusCode);
      res.setEncoding('utf8');

      res.on('data', function (answer) {
        if (answer != 'OK') {
          console.log('Error: ' + answer);
        }
      });
    });

    req.on('error', function (e) {
      console.log('Problem with request: ' + e.message);
    });

    // write date to request body
    req.write(payload);
    req.end();
  });

  sub.on('message', function (channel, message) {
    socket.send(message);
  });

  socket.on('disconnect', function () {
    console.log('disconnected');
  });
});

server.listen(4000, function () {
  console.log('listening at 4000');
});
