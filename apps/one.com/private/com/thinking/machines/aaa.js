function process(request,response)
{
var nn=request.getParameter("nm");
var ss=request.getParameter("sex");
var cc=request.getParameter("ct");
console.log("Request arrived");
console.log("DATA Arrived");
console.log("Name:"+nn);
console.log("Gender:"+ss);
console.log("City :"+cc);
response.writer("<!Doctype html>");
response.writer("<html lang='en'>");
response.writer("<meta charset='utf-8'>");
response.writer("<title>one.com</title>");
response.writer("</head>");
response.writer("<body>");
response.writer("<h1>DATA SAVED</h1></body><html>");
}
module.exports.process=process;
