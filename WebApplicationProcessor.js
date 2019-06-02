var fs=require('fs')
var contextMap=new Map();
var confData={};
var contextNames=fs.readdirSync('./apps');
function WebApplication(vhomepage="",vmapping={})
{
var homepage=vhomepage;
var mapping=vmapping;
this.setHomepage=function(xHomepage){
homepage=xHomepage;
};
this.getHomepage=function()
{
return homepage;
}
this.setMapping=function(xMapping)
{
mapping=xMapping;
};
this.getMapping=function()
{
return mapping;
};
}

function loadConfiguration()
{
try
{
var serverData=JSON.parse(fs.readFileSync('./server.conf'));
}catch(err)
{
console.log("server.conf not found.");
}
return serverData;
}

function loadDataStructure()
{
contextNames.forEach(function(contextName){
webApplication=new WebApplication();
try
{
var confFilePath='./apps/'+contextName+'/private/app.conf';
//console.log("Conf file path "+confFilePath);
confData=JSON.parse(fs.readFileSync(confFilePath));
webApplication.setHomepage(confData["homepage"]);
webApplication.setMapping(confData["mapping"]);
contextMap.set(contextName,webApplication);
}catch(err)
{
contextMap.set(contextName,webApplication);
console.log("app.conf not found.");
}
});

return contextMap;
}

module.exports.loadConfiguration=loadConfiguration;
module.exports.loadDataStructure=loadDataStructure;
