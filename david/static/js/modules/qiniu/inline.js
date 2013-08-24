var $ = require('/jquery');
var _ = require('/lodash');


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
  var self = this;
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
  }).on('click', '.save-item', function(e) {
    e.preventDefault();
    var node = $(this).closest('.uploaded-item')
    var data = node.data();
    $.ajax({
      url: '/api/attachment/' + data.id,
      type: 'POST',
      dataType: 'json',
      data: {
        // add csrf here
      }
    }).success(function(e) {
      
    });
  });
};
InlineUploader.prototype.render_uploaded = function(data) {
  if (!_.isArray(data)) {
    console.log(data);
    return;
  }

  var self = this;
  var list = self.container.find('.uploaded');

  _.forEach(data, function(item) {
    item.filename = item.filename || '';
    item.thumb_url = item.thumb_url || '';
    list.append(self._tmpl_uploaded_item(item));
  });
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

