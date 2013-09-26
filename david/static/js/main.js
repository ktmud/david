require.register('jquery', function(exports, require, module) {
  window._old_jquery = window.jQuery;

  //@import ./lib/jquery.js

  // we don't want to touch any globals
  if (window._old_jquery) {
    window.jQuery = window.$ = window._old_jquery;
  }
});

require.register('main', function(exports, require, module) {
  var jQuery = $ = require('/jquery');

  module.exports = function() {
    window._main_loaded = true;
    $.fn.hover_toggle = function(fn1, fn2) {
      this.each(function(i, item) {
        var trigger = $(this);
        var t = 0;
        trigger.hover(function(e) {
          var self = this;
          clearTimeout(t);
          fn1.call(self);
        }, function(e) {
          var self = this;
          clearTimeout(t);
          t = setTimeout(function() {
            fn2.call(self);
          }, 100);
        });
      });
    };
    $('.has-submenu').hover_toggle(function() {
      $(this).addClass('active');
    }, function() {
      $(this).removeClass('active');
    });
    $('.carousel').hammer().on('swipeleft', function(e) {
      $(this).carousel('next');
    }).on('swiperight', function() {
      $(this).carousel('prev');
    });
  };

  //@import ./lib/bootstrap.js
});

if (!window._main_loaded) {
  require('main')();
}
