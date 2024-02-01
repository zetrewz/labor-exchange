function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {
    $(".resume-favorites-button").each(function () {
        var button = $(this);
        var pk = button.data('pk');
        var appliedKey = "added_" + pk;

        $.ajax({
            url: "/favorite/status/resume/" + pk + "/",
            type: "GET",
            dataType: "json",
            success: function (data) {
                if (data.applied) {
                    setButtonState(true);
                } else {
                    setButtonState(false);
                }
            },
            error: function (xhr, status, error) {
                console.error("Error:", xhr, status, error);
            }
        });

        button.click(function () {
            if (button.hasClass("btn-danger")) {
                $.ajax({
                    url: "/favorite/resume/" + pk + "/",
                    type: "POST",
                    dataType: "json",
                    headers: {
                        "X-CSRFToken": getCookie('csrftoken')
                    },
                    success: function (data) {
                        console.log("Success response:", data);
                        setButtonState(false);
                    },
                    error: function (xhr, status, error) {
                        console.error("Error:", xhr, status, error);
                    }
                });
            } else {
                $.ajax({
                    url: "/favorite/resume/" + pk + "/",
                    type: "POST",
                    dataType: "json",
                    headers: {
                        "X-CSRFToken": getCookie('csrftoken')
                    },
                    success: function (data) {
                        console.log("Success response:", data);
                        setButtonState(true);
                    },
                    error: function (xhr, status, error) {
                        console.error("Error:", xhr, status, error);
                    }
                });
            }
        });

        function setButtonState(applied) {
            if (applied) {
                button.removeClass("btn-light").addClass("btn-danger").prop("disabled", false);
            } else {
                button.removeClass("btn-danger").addClass("btn-light").prop("disabled", false);
            }
        }
    });
});
