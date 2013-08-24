require.register('jquery', function(exports, require, module) {
  //@import ./lib/jquery.js
});

require.register('main', function(exports, require, module) {
  window.jQuery = window.$ = require('/jquery');
  //@import ./lib/bootstrap.js
  window._main_loaded = true;
});

if (!window._main_loaded) {
  require('main');
}

console.log('a');
