function process(request,response)
{
var nn=request.getParameter("nm");
var ss=request.getParameter("sex");
var cc=request.getParameter("ct");
console.log("Request arrived");
console.log("Data arrived");
console.log("Name : "+nn);
console.log("Sex : "+ss);
console.log("City : "+cc);
response.writer("<!Doctype html>");
response.writer("<html lang='en'>");
response.writer("<head>");
response.writer("<meta charset='utf-8'>");
response.writer("<title>three.com</title>");
response.writer("</head>");
response.writer("<body>");
response.writer("<center>");
response.writer("<h1>Session Tracking Example</h1>");
response.writer("<h4><u>Using URL Rewriting</u></h4>");
response.writer("<h1>Data Saved</h1></body></html>");
response.writer("Name : "+nn+"</br>");
response.writer("Gender : "+ss+"</br>");
response.writer("City : "+cc+"</br>");
response.writer("</center>");
}
module.exports.process=process;
