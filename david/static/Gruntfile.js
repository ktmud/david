var fs = require('fs');

function md5(contents) {
  var shasum = crypto.createHash('md5');
  shasum.update(contents);
  return shasum.digest('hex').slice(0, 10);
}
function getHash(f){
  return md5(fs.readFileSync(f, 'utf-8'));
}

module.exports = function(grunt) {
  'use strict';

  var hash_cache = {};
  var dist_hash_cache = {};
  try {
    hash_cache = grunt.file.readJSON('./source_hash.json');
    dist_hash_cache = grunt.file.readJSON('./dist/hash.json');
    for (var k in dist_hash_cache) {
      if (!grunt.file.exists('./dist/' + k)) {
        grunt.log.writeln('!! Missing ' + k.cyan);
        delete dist_hash_cache[k];
      }
    }
  } catch (e) {
    console.error(e);
  }


  function hash_check(f) {
    f = f.replace('./dist/', '');
    // old hash !== new hash
    if (f in dist_hash_cache && hash_cache[f] == getHash(f)) {
      grunt.log.writeln('Skipping ' + f.cyan + ' ..');
      return false;
    }
    return true;
  }

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    meta: {
      src: './',
      dest: './dist',
      oz: {
        baseUrl: './js/',
        distUrl: './dist/js/'
      },
      banner: '/*! Tongdawei.cc - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' Licensed <%= pkg.license %> */\n'
    },
    uglify: {
      options: {
        banner: '<%= meta.banner %>',
      },
      //static_mappings: {
      //},
      dynamic_mappings: {
        files: [
          {
            expand: true,
            cwd: './dist/js/',
            // filename wish under dash will be ignored
            src: ['**/*.js', '!**/*_*.js'],
            dest: 'tmp/js/',
            filter: hash_check,
          }
        ]
      }
    },
    includes: {
      options: {
        includeRegexp: /^\s*(?:\/\/|\/\*)?\s*[\@\#]*(?:include|import)\s+[\"\'\(]*([^\"\'\)]+?)[\"\'\)]*\;?\s*(?:\*\/)?$/,
        duplicates: false,
      },
      js: {
        cwd: './js/',
        src: ['**/*.js'],
        dest: './dist/js/'
      },
      css: {
        cwd: './css/',
        src: '**/*.css',
        dest: './dist/css/'
      }
    },
    wrapper: {
      options: {
        // wrap indicator
        wrap: 'module.exports',
      },
      js: {
        cwd: './dist/js/',
        src: ['**/*.js', '!**/*_*.js'],
        dest: './dist/js/'
      },
    },
    stylus: {
      compile: {
        options: {
          paths: ['./styl', './'],
          urlfunc: 'embedurl',
          import: [
            'nib',
            'base/feel',
          ],
        },
        files: [
          {
            expand: true,
            cwd: './styl/',
            src: ['base.styl', 'admin.styl'],
            dest: './dist/css/',
            ext: '.css'
          }
        ]
      }
    },
    cssmin: {
      compress: {
        files: [
          {
            expand: true,
            cwd: './dist/css/',
            src: ['**/*.css', '!**/*_*.css'],
            dest: 'tmp/css/',
            filter: hash_check,
          }
        ]
      },
    },
    hashmap: {
      options: {
        output: './dist/hash.json',
        rename: false,
        merge: true,
      },
      source_hash: {
        options: {
          output: './source_hash.json',
          encoding: 'utf-8',
          rename: false,
          merge: false,
        },
        cwd: './dist/',
        src: ['**/*.js', '!**/*_*.js', '**/*.css', '!**/*_*.css'],
      },
      js: {
        cwd: 'tmp/',
        src: ['js/**/*.js'],
        dest: './dist/',
      },
      css: {
        cwd: 'tmp/',
        src: ['css/**/*.css'],
        dest: './dist/',
      }
    },
    watch: {
      js: {
        files: ['./js/**/*.js', './bower_components/**/*.js'],
        tasks: ['dist_js']
      }, 
      css: {
        files: ['./styl/**/*.styl', './css/**/*.css'],
        tasks: ['dist_css']
      }
    },
    clean: {
      tmp: {
        src: ['tmp/./js', 'tmp/./css']
      },
      hash: {
        src: ['./source_hash.json', './dist/hash.json']
      },
      js: {
        src: ['./dist/js/']
      },
      css: {
        src: ['./dist/css/']
      }
    },
  });

  // Default task.
  grunt.registerTask('dist_js', ['includes:js', 'wrapper:js']);
  grunt.registerTask('dist_css', ['stylus', 'includes:css']);

  //grunt.registerTask('deps', ['copy:deps']);

  grunt.registerTask('default', ['clean', 'dist_js', 'dist_css']);

  grunt.registerTask('build', ['clean:tmp', 'dist_js', 'dist_css', 'uglify', 'cssmin', 'hashmap']);

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  //grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');

  grunt.loadNpmTasks('grunt-hashmap');

  grunt.loadNpmTasks('grunt-includes');
  //grunt.loadNpmTasks('grunt-istatic');

  var path = require('path');

  grunt.registerMultiTask('wrapper', 'Wrap things up.', function() {
    var opts = this.options({
      head: 'require.register("<%= path %>", function(exports, require, module) {\n',
      nowrap: /(\@nowrap|require\.register)/,
      wrap: null,
      tail: '\n}); require.alias("<%= path %>", "<%= filename %>");'
    });

    this.files.forEach(function(f) {
      var cwd = f.cwd;
      var src = f.src.filter(function(p) {
        p = cwd ? path.join(cwd, p) : p;
        if (grunt.file.exists(p)) {
          return true;
        } else {
          grunt.log.warn('Source file "' + p + '" not found.');
          return false;
        }
      });

      var isfile = grunt.file.isFile(f.dest);

      var flatten = f.flatten;

      src.forEach(function(p) {
        var save_name = flatten ? path.basename(p) : p;
        var dest_file = isfile ? f.dest : path.join(f.dest, save_name);

        p = cwd ? path.join(cwd, p) : p;

        var data = { path: save_name, fullpath: p, filename: path.basename(p, '.js') };
        grunt.file.write(dest_file, wrap(p, opts, data));
        //grunt.log.oklns('Saved ' + dest_file);
      });

      grunt.log.oklns('All done.');
    });

    function wrap(p, opts, data) {
      if (!grunt.file.isFile(p)) {
        grunt.log.warn('file "' + p + '" not found.');
        return 'Error wrapping "' + p + '".';
      }

      var contents = grunt.file.read(p);

      // 先看有没有表示可以 wrap 为 CommonJS 模块的标识
      if (opts.wrap && contents.search(opts.wrap) == -1) {
        grunt.log.warn('skip ' + p.yellow);
        return contents;
      }
      // 即使有标识，但是文件里明确声明了不 wrap ，那也跳过
      if (contents.search(opts.nowrap) !== -1) {
        grunt.log.warn('skip ' + p.yellow);
        return contents;
      }

      var tmpl_opt = { data: data };
      var head = grunt.template.process(opts.head, tmpl_opt);
      var tail = grunt.template.process(opts.tail, tmpl_opt);

      grunt.log.oklns(p.green);

      return head + contents + tail;

      //contents = contents.split(grunt.util.linefeed);
      //if (contents[0].indexOf(opts.nowrap) !== -1) {
        //contents = contents.slice(1);
      //} else {
        //contens.unshift(head);
        //contents.push(tail);
      //}
      //return contents.join(grunt.util.linefeed);
    }
  });

};
