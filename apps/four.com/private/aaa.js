function process(request,response)
{
var nn=request.getParameter("nm");
var ss=request.getParameter("sex");
var cc=request.getParameter("ct");
response.setCookie("nm",nn);
response.setCookie("ct",cc);
response.setCookie("sex",ss);
console.log("Request Arrived");
console.log("Data arrived");
console.log("Name: "+nn);
console.log("Gender: "+ss);
console.log("City: "+cc);
response.writer("<!Doctype html>");
response.writer("<html lang='en'>");
response.writer("<head>");
response.writer("<meta charset='utf-8'>");
response.writer("<title>four.com</title>");
response.writer("</head>");
response.writer("<body>");
response.writer("<center>");
response.writer("<h1>Session Tracking Example</h1>");
response.writer("<h4><u>Using Cookies</u></h4>");
response.writer("<a href='/four.com/bbb'>Save</a>");
response.writer("</center>");
response.writer("</body>");
response.writer("</html>");
}
module.exports.process=process;
