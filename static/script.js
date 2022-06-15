$(document).ready(function () {
    $('#send_values').submit(function(e) {
        e.preventDefault();
        var $element = $(this);
        var data = $element.serialize();
        $.ajax({
            url: window.location.href,
            type: "POST",
            // dataType: "json",
            // cache: false,
            data: data,
            // contentType: false,
            // processData: false,
            success: function(response) {
                $('#responce').html(response.responce);
            },
            error: function(response) { // Данные не отправлены
                alert('Ошибка. Данные не отправлены.');
            }
        });
    });
});