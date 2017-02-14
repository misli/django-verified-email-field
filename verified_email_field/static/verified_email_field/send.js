function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function send_verification_code(name, url) {
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            email: document.getElementById('id_' + name + '_0').value,
        },
        success: function(msg) {
            document.getElementById('id_' + name + '_1').focus();
        }
    });
}
