function SessionFactory(id,time)
{
return new TMHTTPSession(id,time);
}
function TMHTTPSession(id,time=1800)
{
var data=new Map();
var THIS=this;
this.setAttribute=function(key,value)
{
if(key!=undefined && value!=undefined)
data.set(key,value);
}
this.getAttribute=function(key)
{
if(key!=undefined || data.has(key)) 
return data.get(key); 
else
return null;
}
this.getSessionId()
{
return id;
}

}
module.exports.SessionFactory=SessionFactory;