var _ = require('/lodash');


/**
 * Make pics info suitable for carousel render
 */
function _carouselize(pics){
  return pics.map(function(item, i) {
    return { img: item.large_url };
  });
}

function Magazine(container, data, active){
  var self = this;
  self.container = $(container);
  self.init(data, active);
}

Magazine.prototype._tmpl = _.template($.trim($('#tmpl-carousel').html()));

Magazine.prototype.init = function(data, active) {
  var self = this;

  if (active < 0) {
    active += data.pics.length;
  }

  self.data = data;
  self.active = active;
  self.render();

  self.container.find('.carousel').carousel({
    interval: false,
    wrap: false
  }).on('slid.bs.carousel', function() {
    self.active = self.container.find('.carousel-inner .active').index();
  }).hammer().on('swipeleft', function(e) {
    $(this).carousel('next');
  }).on('swiperight', function() {
    $(this).carousel('prev');
  });
};
Magazine.prototype.switchTo = function(n) {
  var self = this;
  if (n < 0) {
    n += self.container.find('.carousel-inner .item').length;
  }
  self.container.find('.carousel').carousel(n);
};

Magazine.prototype.render = function() {
  var self = this;
  var data = self.data;

  self.container.html(self._tmpl({
    show_indicators: false,
    show_controls: true,
    active: self.active,
    id: 'magazine-' + data.id,
    items: _carouselize(data.pics)
  }));
};




function MagazineSwitcher(container, showcase, data) {
  var self = this;
  self.container = $(container);
  self.showcase = $(showcase);
  self.init(data);
}

MagazineSwitcher.prototype._tmpl = _.template($.trim($('#tmpl-switcher').html()));

MagazineSwitcher.prototype.init = function(data) {
  var self = this;


  self.tatal = data.items.length;
  self.data = data;
  self.items = {};

  _.each(self.data.items, function(item) {
    self.items[String(item.id)] = item;
  });

  self.container.on('click', '.switch-item', function(e) {
    self.switchTo($(this).data('id'));
    return false;
  });
  self.showcase.on('click', '[data-slide]', function(e) {
    var dir = $(this).data('slide'),
        nodes = self.showcase.find('.carousel-inner .item'),
        index = self.magazine.active;

    if (dir == 'prev' && index === 0) {
      self.prev();
      self._magazine_slide_to = -1;
    } else if (dir == 'next' && index === nodes.length - 1) {
      self.next();
    }
  });

  self.render(data);
  // show the active, or the first one
  self.show(data.items[data.active || 0]);
};

MagazineSwitcher.prototype.render = function() {
  var self = this;
  var data = self.data;
  self.container.html(self._tmpl({
    items: data.items
  }));
};

MagazineSwitcher.prototype.next = function() {
  var self = this;
  var next = self.container.find('.switch-item.active').next();
  self.switchTo(next.data('id'));
};
MagazineSwitcher.prototype.prev = function() {
  var self = this;
  var prev = self.container.find('.switch-item.active').prev();
  self.switchTo(prev.data('id'));
};
MagazineSwitcher.prototype.switchTo = function(id) {
  if (!id) return;

  var self = this;
  var item = _.isObject(id) ? id : self.items[String(id)];

  self.showcase.stop().fadeTo(200, 0.01, function() {
    self.show(item);
  });
};

MagazineSwitcher.prototype.show = function(item) {
  var self = this;

  // one time use prop
  var slide_to = self._magazine_slide_to || 0;
  if (slide_to) {
    self._magazine_slide_to = 0;
  }
  self.magazine = new Magazine(self.showcase, item, slide_to);

  var node = self.container.find('.switch-item[data-id=' + item.id + ']');

  node.addClass('active').siblings().removeClass('active');

  self.showcase.stop().fadeTo(100, 1);
  setTimeout(function() {
    self.centerize(node);
  }, 200);
};

/**
 * to always keep current item in the center
 */
MagazineSwitcher.prototype.centerize = function(elem) {
  var self = this,
      list = self.container.find('.switch-list'),
      current = self.container.find(elem),
      pos = current.position(),
      item_center = current.width() / 2,
      min = Math.min(0, self.container.width() - list.width()),
      outter_center = self.container.width() / 2;

  list.stop().animate({
    marginLeft: Math.max(Math.min(-pos.left - item_center + outter_center, 0), min)
  }, 300);
};




module.exports = function(switcher, showcase, data) {
  var switcher = new MagazineSwitcher(switcher, showcase, data);
  return switcher;
};
