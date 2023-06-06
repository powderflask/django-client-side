/*
 * CSRF Token:
 *  - provide service for other modules that need the CSRFToken header
 *  - ensure the CSRF Header is set globally for all AJAX requests.
 */
var AjaxCSRFtokenManager = {

    // Utility to set the CSRF cookie in AJAX header -- should probably be moved somewhere more generic?
    // From: https://docs.djangoproject.com/en/1.8/ref/csrf/#ajax
    _getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie) {
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
    },

    csrfSafeMethod: function(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    },

    getRequestHeader: function() {
        return {"X-CSRFToken": this._getCookie('csrftoken')}
    },

    setRequestHeader: function(xhr, method, crossDomain) {
        if (!this.csrfSafeMethod(method) && !crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", this._getCookie('csrftoken'));
        }

    }
};

$(document).ready(function() {
    $(document).ajaxSend(function(event, xhr, settings) {
        AjaxCSRFtokenManager.setRequestHeader(xhr, settings.type, this.crossDomain );
    });
});

module.exports = AjaxCSRFtokenManager;