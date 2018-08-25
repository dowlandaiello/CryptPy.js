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