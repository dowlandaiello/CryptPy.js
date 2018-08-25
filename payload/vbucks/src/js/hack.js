// const fs = require('fs');
// const path = require('path');
// var file_path = path.join(__dirname, 'files/gop2p.go');
// var file_code = "";
// fs.readFile(filePath, {encoding: 'utf-8'}, function(err, data) {
//     if (!err) {
//         file_code = data;
//         console.log('received data: ' + data);
//         response.end();
//     } else {
//         console.log(err);
//     }
// });

// var typed = new Typed('.typed', {
//     strings: [file_code],
//     typeSpeed: 300
// });

var typed = new Typed('.typed', {
    strings: ["Hello, world!"],
    typeSpeed: 300
});