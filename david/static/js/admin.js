// @import ./lib/bootstrap.datepicker.js

var $ = require('/jquery');


exports.init_datepicker = function init_datepicker() {
  $('[data-role=datepicker]').datepicker();
  $('[data-role=datetimepicker]').datepicker({displayTime: true});
};

exports.init = function() {
  this.init_datepicker();
};


module.exports = exports;
