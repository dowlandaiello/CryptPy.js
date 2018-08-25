const electron = require('electron')
const {ipcMain} = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')
const url = require('url')

let loginWindow
let viewWindow
function createLoginWindow () {
  loginWindow = new BrowserWindow({width: 350, height: 410})
  loginWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))
  // loginWindow.webContents.openDevTools()
  loginWindow.on('closed', function () {
    loginWindow = null
  })
}
exports.createViewWindow = () => {
  viewWindow = new BrowserWindow({width: 1080, height: 720, fullscreen: true})
  viewWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'view.html'),
    protocol: 'file:',
    slashes: true
  }))
  // viewWindow.webContents.openDevTools()
  viewWindow.on('closed', function () {
    viewWindow = null
  })
  loginWindow.close();
}
ipcMain.on('resize-window', (event, width, height) => {
  viewWindow.setSize(width, height)
})
app.on('ready', createLoginWindow)
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
app.on('activate', function () {
  if (loginWindow === null) {
    createLoginWindow()
  }
})
