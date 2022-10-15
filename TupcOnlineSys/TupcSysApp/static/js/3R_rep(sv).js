function openNav() {

    var y = document.getElementById("mySidebar");
    var x = document.getElementById("open");
    var z = document.getElementById("close");

    y.style.display = "block";
    x.style.display = "block";
    z.style.display = "block";


}

function closeNav() {

    var y = document.getElementById("mySidebar");
    var x = document.getElementById("close");
    var z = document.getElementById("open");

    y.style.display = "none";
    x.style.display = "block";
    z.style.display = "block";

}

//breadcrumb navigation 

function borrow() {
    var y = document.getElementById("form1");
    var x = document.getElementById("form2");

    y.style.display = "block";
    x.style.display = "none";

}


function requestforpassreset() {

    var y = document.getElementById("form1");
    var x = document.getElementById("form2");

    y.style.display = "none";
    x.style.display = "block";

}