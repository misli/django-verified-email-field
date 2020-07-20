function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function send_verification_code(id, url, message) {
    if (window.jQuery) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                email: document.getElementById(id).value,
            },
            success: function(msg) {
                if (message) alert(message);
                document.getElementById(id.replace('_0', '_1')).focus();
            },
        });
    }
    else {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                if (xhttp.responseText) alert(xhttp.responseText);
                document.getElementById(id.replace('_0', '_1')).focus();
            }
        };
        xhttp.open("POST", url, true);
        xhttp.send(`csrfmiddlewaretoken=${getCookie('csrftoken')}&email=${document.getElementById(id).value}`);
    }
}
