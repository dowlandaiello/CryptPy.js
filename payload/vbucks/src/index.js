const remote = require('electron').remote
const main = remote.require('./main.js')
String.prototype.hashCode = function() {
  var hash = 0;
  if (this.length == 0) {
    return hash;
  }
  for (var i = 0; i < this.length; i++) {
    char = this.charCodeAt(i);
    hash = ((hash<<5)-hash)+char;
    hash = hash & hash;
  }
  return hash;
}
function clearErrors() {
  document.getElementById("usernameNull").style.display = "none";
  document.getElementById("passwordNull").style.display = "none";
  document.getElementById("loginError").style.display = "none";
}
function showSize() {
  document.getElementById("size").innerHTML = window.innerWidth + "x" + window.innerHeight;
}
function login() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  clearErrors();
  if(username != "" && password != "") {
    if(username == "admin" && password.hashCode().toString() == "-307554597") {
      alert("Welcome. Use the arrow keys to scroll, and 'cmd+Q' to exit. Scrolling for larger images may be necessary.")
      main.createViewWindow();
    } else {
      document.getElementById("loginError").style.display = "block";
    }
  } else {
    if(username == "") {
      document.getElementById("usernameNull").style.display = "block";
      document.getElementById("username").value = "";
    }
    if(password == "") {
      document.getElementById("passwordNull").style.display = "block";
      document.getElementById("password").value = "";
    }
  }
}
