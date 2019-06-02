function process(request,response)
{
var nn=request.getParameter("nm");
console.log(nn);
response.writer("<!Doctype html>");
response.writer("<html lang='en'>");
response.writer("<head>");
response.writer("<meta charset='utf-8'>");
response.writer("<title>two.com</title>");
response.writer("<script>");
response.writer("function ramu(f)");
response.writer("{");
response.writer("if(f.sex[0].checked==false && f.sex[1].checked==false)");
response.writer("{");
response.writer("alert(\"Select gender\");");
response.writer("return false;");
response.writer("}");
response.writer("return true;");
response.writer("}");
response.writer("</script>");
response.writer("</head>");
response.writer("<body>");
response.writer("<center>");
response.writer("<h1>Session Tracking Example</h1>");
response.writer("<h4><u>Using Hidden Form Field</u></h4>");
response.writer("<h2>Personal Information - Page 2</h2>");
response.writer("Name : <b>"+nn+"</b></br>");
response.writer("<form action='/two.com/bbb' onsubmit='return ramu(this)'>");

response.writer("<input type='hidden' name='nm' id='nm' value='"+nn+"'>");
response.writer("<table border='0'>");
response.writer("<tr><td>");
response.writer("Gender</td><td>");
response.writer("Male <input type='radio' name='sex' id='ml' value='M'>");
response.writer("&nbsp;&nbsp;&nbsp;");
response.writer("Female <input type='radio' name='sex' id='fe' value='F'>");
response.writer("</td></tr>");
response.writer("</tr><tr>");
response.writer("<td colspan='2' align='center'>");
response.writer("<input type='submit' value='Next'></td></tr></table>");
response.writer("</form>");
response.writer("</center>");
response.writer("</body>");
response.writer("</html>");
}
module.exports.process=process;
