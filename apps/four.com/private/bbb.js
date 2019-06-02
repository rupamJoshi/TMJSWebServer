function process(request,response)
{
console.log("bbb....");
var cookies=request.getCookies();
nn=cookies.nm;
ss=cookies.sex;
cc=cookies.ct;
console.log("Request arrived at bbb");
console.log("Data arrived");
console.log("Name "+nn);
console.log("Gender :"+ss);
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
response.writer("<h1>Data Saved</h1></body></html>");
response.writer("Name : "+nn+"</br>");
response.writer("Gender : "+ss+"</br>");
response.writer("City : "+cc+"</br>");
response.writer("</center>");

}
module.exports.process=process;
