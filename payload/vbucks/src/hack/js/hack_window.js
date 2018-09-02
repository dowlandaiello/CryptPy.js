/*jshint esversion: 6 */

const remote = require('electron').remote;
const main = remote.require('./main.js');
const fs = require('fs');
const path = require('path');

var HACKWINDOW = HACKWINDOW || (function() {
    var _args = {}; // private
    var file_path;
    return {
        init : function(Args) {
            _args = Args;
            file_path = path.join(__dirname, _args[0]);
        },
        close : function() {
            console.log("before closing");
            main.close_hacking_windows();
        },
        main : function() {
            fs.readFile(file_path, 'utf8', function(err, code) {
                if (err) throw err;
                var typed = new Typed('.typed', {
                    strings: [code],
                    typeSpeed: 0
                });
                console.log("typed.js done");
                // setTimeout(close, 14000);
            });
        }
    };
}());