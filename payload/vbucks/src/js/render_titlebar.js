let os = process.platform;
const ElectronTitlebarWindows = require("electron-titlebar-windows");
let title_bar;
if(os == "win32") {
    const remote = require("electron").remote;
    const main = remote.require("./main.js");
    title_bar = new ElectronTitlebarWindows("darkMode");
    title_bar.appendTo(document.getElementById("title_bar"));
    console.log("added");
    title_bar.on("close", function(e) {
        main.titlebar_action("close");
    });
    title_bar.on("minimize", function(e) {
        main.titlebar_action("minimize");
    });
    title_bar.on("maximize", function(e) {
        
        if (main.is_fullscreen() == true) {
            main.titlebar_action("normal");
        } else {
            main.titlebar_action("maximize");
        }
    });
}