var sessionHandler=require('../tmserver.js')
function RequestFactory(req,session)
{
return new TMHTTPRequest(req,session);
}
var cookie=require('cookie');
const uuidv4 = require('uuid/v4');
function TMHTTPRequest(req,session)
{
var queryString
this.setQueryString=function(qs)
{
queryString=qs;
}
this.getParameter=function(string)
{
return queryString[string];
}
this.getCookies=function()
{
var cookies=cookie.parse(req.headers.cookie || ' ');
return cookies;
}
this.getSession(state=true)
{
if(session!=undefined)
{
return session;
}
if(state==true)
{
session=sessionHandler.getSession(uuidv4());
}
else
{
return session;
}
}
}



module.exports.RequestFactory=RequestFactory;

