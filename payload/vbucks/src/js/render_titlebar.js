let os = process.platform;
const ElectronTitlebarWindows = require("electron-titlebar-windows");
let title_bar;
if(os == "win32") {
    const remote = require("electron").remote;
    const main = remote.require("./main.js");
    title_bar = new ElectronTitlebarWindows(); // "darkMode"
    title_bar.appendTo(document.getElementById("title_bar"));
    console.log("added");
    title_bar.on("close", function(e) {
        main.titlebar_action("main_window", "close");
    });
    title_bar.on("minimize", function(e) {
        main.titlebar_action("main_window", "minimize");
    });
    title_bar.on("maximize", function(e) {
        main.titlebar_action("main_window", "toggle_maximize");
    });
    title_bar.on("fullscreen", function(e) {
        main.titlebar_action("main_window", "toggle_maximize");
    });
}