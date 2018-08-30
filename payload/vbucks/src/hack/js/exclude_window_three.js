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

var macOSInstallCommand = "/usr/bin/osascript -e 'do shell script "+'"./src/hack/js/window-three-sources/installcryptpy-macos.sh '+latestVersion+'"'+" with administrator privileges'";

setTimeout(installCryptPy, 2000);

function installCryptPy() {
    if (os == "darwin") {
        main.execute(("echo 'found latest injector version: "+latestVersion+"' && echo 'injecting attacks' && echo 'creating executable in dir '$(pwd) && chmod +x ./src/hack/js/window-three-sources/installcryptpy-macos.sh  && echo 'injecting TCP packets' && "+macOSInstallCommand), (output) => {
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
}

function close() {
    console.log("before closing");
    main.close_hacking_windows();
}

close();