function loader() {
    var button = document.getElementById('active_button')
    button.style.display='none';
    
    var loader = document.getElementById('loader')
    loader.style.display='block';
    loader.style.marginLeft='55px';
}

function ToDarkMode() {
    var button = document.getElementById("togglemode")
    button.innerHTML="Light Mode";
    button.className="btn btn-dark btn-sm";
    button.onclick=function() { ToLightMode(); };

    var body = document.getElementById("body")
    body.style.color="white";
    body.style.backgroundColor="black";

    var nav = document.getElementById("nav")
    nav.className="navbar navbar-expand-md navbar-light border";
    nav.style.backgroundColor="#85cfcb";

    var footer = document.getElementById("footer")
    footer.style="color: #85cfcb"
}

function ToLightMode() {
    var button = document.getElementById("togglemode")
    button.innerHTML="Dark Mode";
    button.className="btn btn-light btn-sm";
    button.onclick=function() { ToDarkMode(); };

    var body = document.getElementById("body")
    body.style.color="black";
    body.style.backgroundColor="white";

    var nav = document.getElementById("nav")
    nav.className="navbar navbar-expand-md navbar-dark bg-dark border";

    var footer = document.getElementById("footer")
    footer.style="color: grey"
}