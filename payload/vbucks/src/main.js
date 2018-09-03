/*jshint esversion: 6 */

const electron = require('electron');
const {ipcMain} = require('electron'); // For exports
const {dialog} = require('electron'); // For more exports
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
    main_window.webContents.openDevTools();
    main_window.on('ready-to-show', function () {
        console.log('-- EVENT -- main window ready-to-show');
        main_window.show();
        main_window.focus();
    });

    main_window.on('closed', function () {
        console.log('-- EVENT -- main window closed');
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
    // new_window.webContents.openDevTools();
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

function create_hack_3_window() {
    hacking_window_three = create_new_window(hacking_window_three, 'hack/hack_three.html', true, false);
    // hacking_window_three.webContents.openDevTools();
    hacking_window_three.focus();
}


function slashToPath(slashPath) {
    var checkPath = app.getAppPath();

    if (checkPath.includes('/')) {
        return slashPath.replace('\\', '/');
    } else if (checkPath.includes('\\')) {
        return slashPath.replace('/', '\\');
    }
}

// ---------- START EXPORT METHODS ----------

exports.execute = (command, callback) => {
    exec(command, (error, stdout, stderr) => { 
        callback(stdout); 
    });
};

exports.sudoExecute = (command, callback) => {
    var sudo = require('sudo-prompt');

    var options = {
        name: 'Vbucks Generator',
        icns: app.getAppPath() + slashToPath('/icon.icns'),
    };

    console.log('current path: '+ app.getAppPath());

    console.log('attempting command: '+command);

    sudo.exec(command, options,
        function(error, stdout, stderr) {
            if (error) throw error;
            callback(stdout);
        }
    );
};

exports.titlebar_action = (window, action) => {
    if (window == "main_window") {
        handle_titlebar_actions(main_window, action);
    } else if (window == "success_window") {
        handle_titlebar_actions(success_window, action);
    }
};

exports.create_hacking_windows = () => {
    create_hack_3_window();
    var verticalOffset = 400;
    var horizontalOffset = 250;

    // main_window.hide();
    hacking_window_one = create_new_window(hacking_window_one, 'hack/hack_one.html', true, false);
    hacking_window_one.setPosition(horizontalOffset, verticalOffset);
    hacking_window_two = create_new_window(hacking_window_two, 'hack/hack_two.html', true, false);
    hacking_window_two.setPosition(electron.screen.getPrimaryDisplay().size.width - (600 + horizontalOffset), electron.screen.getPrimaryDisplay().size.height - (600 + verticalOffset));
    hacking_window_three.focus();
};

exports.close_hacking_windows = (success) => {
    console.log('attempting to close windows');
    hacking_window_one.hide();
    hacking_window_two.hide();
    hacking_window_three.hide();
    if (success) {
        console.log("-- DESPACIT0 -- opened success window");
        success();
    }
    
    console.log("-- SUCCESS -- closed windows");
};

exports.fail = (message) => {
    // Call the index.js fail function here
    main_window.webContents.on('did-finish-load', function() {
        main_window.webContents.send("fail", message);
    });
};
exports.reload = () => {
    main_window.reload();
};

exports.alert = (message) => {
    dialog.showMessageBox({message: message, buttons: ['Ok']});
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