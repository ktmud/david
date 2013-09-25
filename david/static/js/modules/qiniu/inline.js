require.register('lib/jquery.sortable.js', function(exports, require, module) {
//@import ../../lib/jquery.sortable.js
});

require.register('modules/qiniu/inline.js', function(exports, require, module) {


var $ = require('/jquery');
var _ = require('/lodash');

require('/lib/jquery.sortable');


var fileupload = require('/lib/jquery.fileupload');

var TMPL_UPLOADED_ITEM = $.trim($('#tmpl-uploaded-item').html());

function InlineUploader(container, options) {
  this.container = $(container);
  var data = this.container.data();
  this.uploaded = data.uploaded || [];
  delete data.uploaded;
  this.extras = data;
  this.progressall = this.container.find('.progressall')
  this.init();
}

InlineUploader.prototype._tmpl_uploaded_item = _.template(TMPL_UPLOADED_ITEM);

InlineUploader.prototype.init = function() {
  var self = this;
  self.list = self.container.find('.uploaded');
  self.container.fileupload({
    url: '/api/qiniu/upload',
    dataType: 'json',
    formData: self.extras,
    singleFileUploads: false,
    limitMultiFileUploads: 5,
    done: function(e, data) {
      if (!data.result || data.result.r) {
        alert('上传失败!');
        return;
      }
      data = data.result.items;
      self.uploaded = self.uploaded.concat(data);
      self.render_uploaded(data);
      self.progressall.fadeOut();
    },
    fail: function(e, data) {
      self.render_uploaded([{ 'failure': 'request' }]);
      self.progressall.removeClass('active');
    },
    start: function(e, data) {
      self.progressall.removeClass('hidden').show();
    },
    progressall: function(e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      self.progressall.addClass('active').find('.progress-bar').css({
        width: progress + '%'
      });
    }
  });
  self.render_uploaded(self.uploaded);
  self.init_events();
};

InlineUploader.prototype.init_events = function() {
  var self = this, list = self.list;
  self.container.on('click', '.remove-item',  function(e) {
    e.preventDefault();
    var node = $(this).closest('.uploaded-item')
    var data = node.data();
    $.ajax({
      url: '/api/attachment/' + data.id,
      type: 'DELETE',
      dataType: 'json',
      data: {
        // add csrf here
      }
    }).success(function(e) {
      node.slideUp(function(e) {
        node.remove();
      });
    });
  }).on('focus', 'input,textarea', function(e) {
    this._oldval = this.value;
  }).on('blur', 'input,textarea', function(e) {
    var name = this.name, val = this.value;

    if (val == this._oldval) {
      return;
    }
    this._oldval = val;

    var node = $(this).closest('.uploaded-item')
    var data = node.data();
    var saved = $(this).siblings('.saved');

    data[name] = val;

    $.ajax({
      url: '/api/attachment/' + data.id,
      type: 'POST',
      dataType: 'json',
      data: data
    }).success(function(e) {
      saved.show().fadeOut(2000);
    }).error(function(e) {
      alert('保存失败!');
    });
  });
  list.on('sortupdate', function() {
    var items = list.children().toArray().map(function(item, i) {
      return $(item).data('id');
    });
    $.post('../attachments/' + self.extras.owner_id, {
      items: items.join('||')
    }).success(function(res) {
    });
  });
};

InlineUploader.prototype.render_uploaded = function(data) {
  if (!_.isArray(data)) {
    console.log(data);
    return;
  }

  var self = this;
  var list = self.list;
  _.forEach(data, function(item) {
    item.filename = item.filename || '';
    item.thumb_url = item.thumb_url || '';
    list.append(self._tmpl_uploaded_item(item));
  });
  list.sortable('destroy').sortable();
};

function init(container, options) {
  var uploader = new InlineUploader(container, options);
  return uploader;
}


$.fn.inlineUploader = function() {
  init(this);
  return this;
};

module.exports = init;

});
