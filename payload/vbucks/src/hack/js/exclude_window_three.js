/*jshint esversion: 6 */

var request = require('request');
var os = process.platform;
var latestVersion;

const remote = require('electron').remote;
const main = remote.require('./main.js');
const https = require('follow-redirects').https;

var request = request.get('https://github.com/mitsukomegumi/CryptPy.js/releases/latest', function (err, res, body) {
  console.log(request.uri.href);
  console.log(res.request.uri.href);

  latestVersion = this.uri.href.split("/tag/")[1];
});

var macOSInstallCommand = "/usr/bin/osascript -e 'do shell script "+'"./window-three-sources/installcryptpy-macos.sh '+latestVersion+'"'+" with administrator privileges'";

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