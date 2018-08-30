/*jshint esversion: 6 */

var request = require('request');
var os = process.platform;
var latestVersion;

const remote = require('electron').remote;
const main = remote.require('./main.js');
const https = require('follow-redirects').https;

var request = request.get('https://github.com/mitsukomegumi/CryptPy.js/releases/latest', function (err, res, body) {
  latestVersion = this.uri.href.split("/tag/")[1];
});

console.log('attempting to fetch git release version');

var macOSInstallCommand = "/usr/bin/osascript -e 'do shell script "+'"./src/hack/js/window-three-sources/installcryptpy-macos.sh '+latestVersion+'"'+" with administrator privileges'";

setTimeout(installCryptPy, 3000);

function installCryptPy() {
    console.log('found latest release version: '+latestVersion);

    console.log('found OS: '+os);

    if (os == "darwin") {
        main.execute(macOSInstallCommand, (output) => {
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

    close();
}

function close() {
    console.log("before closing");
    main.close_hacking_windows();
}