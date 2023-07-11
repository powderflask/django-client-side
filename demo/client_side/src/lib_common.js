/**
 * Common 3rd party and custom Components
 *   -- Demo uses npm and broswerify https://www.npmjs.com/package/browserify
 *          to build components into single script
 *
 *   External Dependencies:  Bootstrap 3 + JQuery 3  are pulled from CDN
 */
// include any 3rd party or custom components - for example, grab things from node modules, or this src directory
require('jquery.formset/src/jquery.formset');
require('eonasdan-bootstrap-datetimepicker');
require('./ajax/csrftoken');

/*
 *  Enable common widgets and JS interactions across entire site .
 */
$(document).ready(function() {
    // for example, enable tooltip elements
    $('[data-toggle="tooltip"]').tooltip();

    // replace date fields with a datepicker widget.
    $('input.dateinput').parent().datetimepicker({
        format: 'YYYY-MM-DD',
        useCurrent: false
    });
});

