const fs = require('fs');
const path = require('path');
function random() {
    return Math.floor(Math.random() * 2);
}
var code_files = [
    "files/gop2p.go",
    "files/nblocks.cpp"
]
var file_path = path.join(__dirname, code_files[random()]);

fs.readFile(file_path, 'utf8', function(err, code) {
    if (err) throw err;
    var typed = new Typed('.typed', {
        strings: [code],
        typeSpeed: 0
    })
})
