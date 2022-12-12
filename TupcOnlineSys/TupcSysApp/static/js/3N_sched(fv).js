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

function requestforlab() {
    var a = document.getElementById("tableform1");
    var b = document.getElementById("table2");
    

    a.style.display = "block";
    b.style.display = "none";
  
}


function labsched() {
    var a = document.getElementById("tableform1");
    var b = document.getElementById("table2");
    

    a.style.display = "none";
    b.style.display = "block";
  
}
