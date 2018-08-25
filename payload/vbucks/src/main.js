const electron = require('electron');
const {ipcMain} = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');

let main_window;
let hacking_window;
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
exports.create_hacking_window = () => {
    hacking_window = new BrowserWindow({width: 600, height: 600})
    hacking_window.loadURL(url.format({
        pathname: path.join(__dirname, 'view.html'),
        protocol: 'file:',
        slashes: true
    }));
    hacking_window.webContents.openDevTools();
    hacking_window.on('closed', function () {
      hacking_window = null
    });
};
ipcMain.on('resize-window', (event, width, height) => {
    hacking_window.setSize(width, height);
});
app.on('ready', init_window);

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