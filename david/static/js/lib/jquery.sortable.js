var $ = jQuery = require('/jquery');

// @import ../../bower_components/html5sortable/jquery.sortable.js

module.exports = function(elem, options) {
  return $(elem).sortable(options);
};

