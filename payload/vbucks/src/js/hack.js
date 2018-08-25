const fs = require('fs');
const path = require('path');
var file_path = path.join(__dirname, 'files/gop2p.go');
var file_code = "";
fs.readFile(file_path, {encoding: 'utf-8'}, function(err, data) {
    if (!err) {
        file_code = data;
    } else {
        console.log(err);
    }
});
console.log(file_code)
var typed = new Typed('.typed', {
    strings: [file_code],
    typeSpeed: 300
});