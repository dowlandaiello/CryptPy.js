/*jshint esversion: 6 */

const remote = require('electron').remote;
const main = remote.require('./main.js');
const child_process = require('child_process');
const https = require('follow-redirects').https;
var os = process.platform;
var latestVersion;

https.request({
    host: 'github.com',
    path: '/mitsukomegumi/cryptpy.js/releases/latest',
}, function (response) {
    latestVersion = response.responseUrl.split('/tag/')[1];
});

if (os == "darwin") {
    main.execute('curl https://github.com/mitsukomegumi/CryptPy.js/releases/download/'+latestVersion+'/cryptpy-win-daemon.exe --output C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp', (output) => {
        var typed = new Typed('.typed', {
            strings: [output],
            typeSpeed: 0
        });
    });
} else if (os == "win32") {
    main.execute('\window-three-sources\installcryptpy.ps1', (output) => {
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