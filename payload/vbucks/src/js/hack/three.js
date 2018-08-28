const fs = require('fs');
const path = require('path');
const exec = require('child_process').exec;

function execute(command, callback) {
    exec(command, (error, stdout, stderr) => { 
        callback(stdout); 
    });
}

function close() {
    console.log("before closing");
    main.close_hacking_windows();
}
const remote = require('electron').remote;
const main = remote.require('./main.js');
setTimeout(close, 7000);