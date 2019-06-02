var fs=require('fs');
var http=require('http');
var mime=require('mime-types');
var HTTPRequest=require('./TMHttp/TMHTTPRequest');
var HTTPResponse=require('./TMHttp/TMHTTPResponse');
var HTTPSession=require('./TMHttp/TMHTTPSession');

var webApplicationProcessor=require('./WebApplicationProcessor');
const uuidv4 = require('uuid/v4');

var port=webApplicationProcessor.loadConfiguration()["port"];
var contextNamesDS=webApplicationProcessor.loadDataStructure();
var direct=true;
var queryString={};
var directWebPage=false;


function parseQuery(queryString) {
    var query = {};
    var pairs = (queryString).split('&');
    for (var i = 0; i < pairs.length; i++) {
        var pair = pairs[i].split('=');
        query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
    }
    return query;
}

function SessionData(vContextName,vSession=null)
{
var contextName=vContextName;
var session=vSession;
var request=null;
var response=null;
this.getSession=function()
{
return session;
}
this.setRequest=function(vRequest)
{
request=vRequest;
}
this.setResponse=function(vResponse)
{
response=vResponse;
}
this.getRequest=function()
{
return request;
}
this.getResponse=function()
{
return response;
}
this.setRequestAndResponse=function(vRequest,vResponse)
{
request=vRequest;
response=vResponse;
}
this.isRequestAndResponseExists=function()
{
return request!=null && response!=null;
}
}










function getSession(id=null,req)
{
if(id==null)
{
return getSession(uuidv4());
}
var context=req.url.split('/')[1];
if(id!=null && !sessionDataMap.has(id))
{
var session=HTTPSession.SessionFactory(id);
sessionDataMap[id]=new SessionData(context,session);
if(sessionMap.has(context))
{
sessionMap.get(context).push(session);
}
else
{
sessions=[];
sessions.push(session);
sessionMap.set(context,sessions);
return session;
}
}
else
{
if(sessionDataMap.has(id))
{
return sessionDataMap.get(id).getSession();
}
}

}



function run()
{
http.createServer(function(req,res){
var mimeType=mime.lookup(req.url);
console.log(req.url);
direct=true;
if(req.url.split('/')[2]=='private' || req.url==='/favicon.ico')
{
res.end('404',"NOT FOUND");
return;
}

if(req.url=='/')
{
direct=false;
req.url='./default/index.html';
fs.readFile(req.url,function(err,data){
res.writeHead(200,{'contentType':mimeType});
res.write(data);
res.end();
});
return;
}
else
{
console.log("else mein aaya");
str=req.url.split("/");
if(str.length==2 && req.url!='/favicon.ico')
{
direct=false;
var contextName=str[1];
if(contextNamesDS.get(contextName).getHomepage()!='')
{
var path=contextNamesDS.get(contextName).getHomepage();
res.writeHead(301,{'Location':'http://localhost:8080/'+contextName+'/'+path});
res.end();
}
else
{
if(fs.existsSync('./apps/'+contextName+'/index.html'))
{
res.writeHead(301,{'Location':'http://localhost:8080/'+contextName+'/index.html'});
res.end();

}
else
{
if(fs.existsSync('./apps/'+contextName+'/index.htm'))
{
res.writeHead(301,{'Location':'http://localhost:8080/'+contextName+'/index.htm'});
res.end();
}
else
{
if(fs.existsSync('./apps/'+contextName+'/index.js'))
{
console.log("Not yet implemented");
}
else
{
res.end('404 Not found');
}
}
}
}

}
}
var contextName=req.url.split('/')[1];

var webPageName=req.url.split('/').pop();
console.log(contextName);
if(contextNamesDS.get(contextName).getMapping()[webPageName]!=undefined)
{
console.log("direct Web page:"+webPageName);
directWebPage=true;
}


if(req.url.indexOf('?')!=-1 || directWebPage)
{
direct=false;
console.log(req.url);
if(!directWebPage)
{
qStr=req.url.split('?')[1];
queryString=parseQuery(qStr);
webPageName=req.url.split('?')[0].split('/').pop();
console.log(webPageName);
contextName=req.url.split('?')[0].split('/')[1];
}
packageName=contextNamesDS.get(contextName).getMapping()[webPageName];
console.log(packageName);
if(packageName==undefined)
{
res.end(404,"Resource not found");
}
else
{
packagePath='./apps/'+contextName+'/private/'+packageName.split('.').join('/');
console.log(packagePath);
if(fs.existsSync(packagePath+'.js'))
{
session=getSession();
if(!sessionMap.has(contextName))
{
sessions=[];
sessions.push(session);
sessionMap.set(context,sessions);
}
id=session.getSessionId();
if(!sessionDataMap.has(id))
{
sesssionDataMap.set(id,new SessionData(contextName,session));
}
processObject=require(packagePath);
var request=HTTPRequest.RequestFactory(req,session);
var response=HTTPResponse.ResponseFactory();
request.setQueryString(queryString);
response.setResponseHandler(res,id);
processObject.process(request,response);
}
else
{
res.end(404,"Not Found");
}
}
}


//code for serving resource directly..
if(direct)
{
var path='./apps'+req.url;
console.log(path);
fs.readFile(path,function(error,data){
if(data)
{
res.writeHead(200,{'content-type':mimeType});
res.write(data);
res.end();
}

if(error)
{
console.log(error.message)
res.writeHead(404,{'context-type':'text/html'})
res.end('404 Not found');
}
});
}
}).listen(port);
}
run();
module.exports.getSession=getSession;
