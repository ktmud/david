require.register('gridalicious', function(exports, require, module){

// @import ../../lib/jquery.grid-a-licious.js

});

require.register('modules/gallery/photos', function(exports, require, module){

var _ = require('/lodash');
var Gal = require('/gridalicious');


function PhotoGrid(container, data) {
  this.container = $(container);
  this.init(data);
}

PhotoGrid.prototype._tmpl = _.template($.trim($('#tmpl-photos').html()));

PhotoGrid.prototype.init = function(data) {
  var self = this;
  self.data = data;
  self.gridalicious = new Gal({
    width: 300,
    gutter: 15,
    selector: '.mod'
  }, self.container[0]);

  self.render(data);
  // after first render, it's safe to animate
  self.gridalicious.options.animate = true;
};

PhotoGrid.prototype.render = function(data) {
  var self = this;
  var boxes = $(self._tmpl(data)).filter('.mod');
  self.gridalicious.append(boxes);
};

module.exports = function(container, data) {
  return new PhotoGrid(container, data);
};

});
