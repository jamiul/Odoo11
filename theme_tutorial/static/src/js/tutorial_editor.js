odoo.define('snippet_testimonial_options', function(require) {
    'use strict';
    var options = require('web_editor.snippets.options');
    options.registry.snippet_testimonial_options = options.Class.extend({

        onFocus: function() {

            alert("On focus!")

        },

    });
});