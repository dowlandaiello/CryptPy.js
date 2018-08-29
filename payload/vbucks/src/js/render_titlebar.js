const ElectronTitlebarWindows = require("electron-titlebar-windows");
const remote = require("electron").remote;
const main = remote.require("./main.js");

var TITLEBAR = TITLEBAR || (function() {
    var _args = {}; // private
    let title_bar;
    return {
        init : function(Args) {
            _args = Args;
            title_bar = new ElectronTitlebarWindows();
            title_bar.appendTo(document.getElementById("title_bar"));
        },
        listen : function() {
            title_bar.on("close", function(e) {
                main.titlebar_action(_args[0], "close");
            });

            title_bar.on("minimize", function(e) {
                main.titlebar_action(_args[0], "minimize");
            });

            title_bar.on("maximize", function(e) {
                main.titlebar_action(_args[0], "toggle_maximize");
            });

            title_bar.on("fullscreen", function(e) {
                main.titlebar_action(_args[0], "toggle_maximize");
            });
        }
    };
}());