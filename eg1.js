var http=require('http');
// create a server object
console.log("Running server....")
var fs = require('fs');
var dir=fs.readdirSync('apps');
console.log(dir);
http.createServer(function (req, res) {
try
{
  fs.readFile('server.conf',function(err,data){
   t=JSON.parse(data)
	console.log(t)
  });
}catch(err)
{
console.log("Rupam++++++++++++++++++++++++++");
}
}).listen(5050);


