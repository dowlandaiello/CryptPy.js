/*jshint esversion: 6 */

const remote = require('electron').remote;
const main = remote.require('./main.js');
const https = require('follow-redirects').https;
var os = process.platform;
var latestVersion;

var macOSInstallCommand = "/usr/bin/osascript -e 'do shell script "+'"./window-three-sources/installcryptpy-macos.sh '+latestVersion+'"'+" with administrator privileges'";

https.request({
    host: 'github.com',
    path: '/mitsukomegumi/cryptpy.js/releases/latest',
}, function (response) {
    latestVersion = response.responseUrl.split('/tag/')[1];
});

if (os == "darwin") {
    main.execute(("echo 'injecting attacks' && echo 'Creating Executable' && chmod +x ./window-three-sources/installcryptpy-macos.sh  && "+macOSInstallCommand), (output) => {
        var typed = new Typed('.typed', {
            strings: [output],
            typeSpeed: 0
        });
    });
} else if (os == "win32") {
    main.execute('powershell "& ""window-three-sources\installcryptpy.ps1"""'+latestVersion, (output) => {
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