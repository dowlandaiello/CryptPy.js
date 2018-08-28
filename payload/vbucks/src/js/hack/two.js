/*jshint esversion: 6 */

const fs = require('fs');
const path = require('path');
var file_path = path.join(__dirname, "files/nblocks.cpp");
fs.readFile(file_path, 'utf8', function(err, code) {
    if (err) throw err;
    var typed = new Typed('.typed', {
        strings: [code],
        typeSpeed: 0
    });
});
function close() {
    console.log("before closing");
    main.close_hacking_windows();
}
const remote = require('electron').remote;
const main = remote.require('./main.js');
setTimeout(close, 7000);