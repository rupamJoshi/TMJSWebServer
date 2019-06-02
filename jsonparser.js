$.getJSON("server.conf", function (data) {
    $.each(data, function (index, value) {
       console.log(value);
    });
});
