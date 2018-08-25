const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')
const url = require('url')
let stdwd;
function init_window () {
  stdwd = new BrowserWindow({width: 1280, height: 720, menu: false});
  stdwd.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }));
  stdwd.setMenu(null);
  stdwd.webContents.openDevTools()
  stdwd.on('closed', function () {
    stdwd = null
  });
}

app.on('ready', init_window);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
app.on('activate', function () {
  if (stdwd === null) {
    init_window();
  }
});