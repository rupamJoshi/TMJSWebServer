var http = require('http')
var Cookies = require('cookies')
var keys = ['keyboard cat']
var server = http.createServer(function (req, res) {
 var cookies = new Cookies(req, res,{keys:keys})
 var lastVisit = cookies.get('LastVisit', { signed: true })
 cookies.set('LastVisit','HELLOOOOooo', { signed: true,maxAge:100})
  if (!lastVisit) {
 res.setHeader('Content-Type', 'text/plain')
  res.end('Welcome, first time visitor!')
  } else {
 res.setHeader('Content-Type', 'text/plain')
 res.end('Welcome back! Nothing much changed since your last visit at ' + lastVisit + '.')
}
})
 
server.listen(5050, function () {
  console.log('Visit us at http://127.0.0.1:3000/ !')
})
