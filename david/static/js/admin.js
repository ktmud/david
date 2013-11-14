// @import ./lib/bootstrap.datepicker.js

var $ = require('/jquery');


exports.init_datepicker = function init_datepicker() {
  $('[data-role=datepicker]').datetimepicker({ minView: 'month' });
  $('[data-role=datetimepicker]').datetimepicker();
  $('[data-role=timepicker]').datetimepicker({
    startView: 'day',
    maxView: 'day',
    formatViewType: 'time'
  });
};

exports.init = function() {
  this.init_datepicker();
};


module.exports = exports;
