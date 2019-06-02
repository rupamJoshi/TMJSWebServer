function ResponseFactory()
{
return new TMHTTPResponse();
}


function TMHTTPResponse()
{
var responseHandler;
var mimeType;
var cookie=[];

this.setResponseHandler=function(vResHandler,id){
		responseHandler=vResHandler;
responseHandler.writeHeader(200,{'Set-Cookie':'id='+id});
}
this.writer=function(string)
{
				responseHandler.write(string);
}
this.setContentType=function(mimeType)
{
				responseHandler.setHeader('Content-Type',mimeType);
}
this.setCookie=function(name,value)
{
cookie.push(name+'='+value)
responseHandler.writeHeader(200,{'Set-Cookie':cookie});


}

}

module.exports.ResponseFactory=ResponseFactory;
