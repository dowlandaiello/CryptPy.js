const electron = require('electron');
const {ipcMain} = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');

let main_window;
let hacking_window_one;
let hacking_window_two;

function init_main_window () {
    main_window = new BrowserWindow({width: 1280, height: 720, menu: false});
    main_window.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));
    main_window.setMenu(null);
    // main_window.webContents.openDevTools();
    main_window.on('closed', function () {
        main_window = null
    });
}
function new_window(new_window, page) {
    new_window = new BrowserWindow({width: 600, height: 600})
    new_window.loadURL(url.format({
        pathname: path.join(__dirname, page),
        protocol: 'file:',
        slashes: true
    }));
    new_window.webContents.openDevTools();
    new_window.on('closed', function () {
      new_window = null
    });
    return new_window;
}
exports.create_hacking_windows = () => {
    hacking_window_one = new_window(hacking_window_one, 'hack_one.html')
    hacking_window_two = new_window(hacking_window_two, 'hack_two.html')
};
ipcMain.on('resize-window', (event, width, height) => {
    hacking_window_one.setSize(width, height);
});
app.on('ready', init_main_window);

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
app.on('activate', function () {
    if (main_window === null) {
        init_main_window();
    }
});