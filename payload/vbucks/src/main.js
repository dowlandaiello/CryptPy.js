/*jshint esversion: 6 */

const electron = require('electron');
const {ipcMain} = require('electron'); // For exports
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');
const exec = require('child_process').exec;

let main_window;
let hacking_window_one;
let hacking_window_two;
let hacking_window_three;
let success_window;
let not_created = true;

function init_main_window () {
    main_window = new BrowserWindow({
        titleBarStyle: 'hidden', 
        width: 1280, height: 720,
        menu: false, frame: false,
        show: false
    });

    main_window.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));

    main_window.setMenu(null);
    //main_window.webContents.openDevTools();
    main_window.on('ready-to-show', function () {
        main_window.show();
        main_window.focus();
    });
    main_window.on('closed', function () {
        main_window = null;
    });
}

function create_new_window(new_window, page, no_frame, title_bar_hidden) {
    if (no_frame == true) {
        if (title_bar_hidden == true) {
            new_window = new BrowserWindow({titleBarStyle: 'hidden', width: 600, height: 600, frame: false});
        } else {
            new_window = new BrowserWindow({width: 600, height: 600, frame: false});
        }
    } else {
        new_window = new BrowserWindow({width: 600, height: 600});
    }

    new_window.loadURL(url.format({
        pathname: path.join(__dirname, page),
        protocol: 'file:',
        slashes: true
    }));

    new_window.setMenu(null);
    //new_window.webContents.openDevTools();
    new_window.on('closed', function () {
      new_window = null;
    });
    return new_window;
}

function handle_titlebar_actions(window, action) {
    if (action == "close") {
        window.close();
    } else if (action == "minimize") {
        window.minimize();
    } else if (action == "toggle_maximize") {
        if (window.isMaximized() == true) {
            window.unmaximize();
        } else {
            window.maximize();
        }
    } else {
        console.log("invalid titlebar action");
    }
}

function success() {
    success_window = create_new_window(success_window, 'success.html', true, false);
    success_window.show();
    success_window.focus();
}

// ---------- START EXPORT METHODS ----------

exports.execute = (command, callback) => {
    exec(command, (error, stdout, stderr) => { 
        callback(stdout); 
    });
};

exports.titlebar_action = (window, action) => {
    if (window == "main_window") {
        handle_titlebar_actions(main_window, action);
    } else if (window == "success_window") {
        handle_titlebar_actions(success_window, action);
    }
}

exports.create_hack_3_window = () => {
    main_window.hide();
    hacking_window_three = create_new_window(hacking_window_three, 'hack/hack_three.html', true, false);
}

exports.create_hacking_windows = () => {
    hacking_window_one = create_new_window(hacking_window_one, 'hack/hack_one.html', true, false);
    hacking_window_one.setPosition(200, 200);
    hacking_window_two = create_new_window(hacking_window_two, 'hack/hack_two.html', true, false);
    hacking_window_two.setPosition(600, 0);
    hacking_window_three.focus();
};

exports.close_hacking_windows = () => {
    console.log('attempting to close windows')

    hacking_window_one.hide();
    hacking_window_two.hide();
    hacking_window_three.hide();
    
    success_window = create_new_window(success_window, 'success.html', true, true);
    success_window.show();
    success_window.focus();

    console.log("-- SUCCESS -- closed windows");
};

// ---------- END EXPORT METHODS ----------

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
