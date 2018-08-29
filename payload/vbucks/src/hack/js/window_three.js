/*jshint esversion: 6 */

const remote = require('electron').remote;
const child_process = require('child_process');
var os = process.platform;

if (os == "darwin") {
    main.execute('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', (output) => {
        var typed = new Typed('.typed', {
            strings: [output],
            typeSpeed: 0
        });
    });
} else if (os == "win32") {
    

    child_process.exec('path_to_your_executables', function(error, stdout, stderr) {
    console.log(stdout);
});
    main.execute('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"', (output) => {
        var typed = new Typed('.typed', {
            strings: [output],
            typeSpeed: 0
        });
    });
}

function close() {
    console.log("before closing");
    main.close_hacking_windows();
}

setTimeout(close, 7000);