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

function reportandmaintenance() {
    var w = document.getElementById("table4")
    var y = document.getElementById("table1");
    var x = document.getElementById("table2");
    var z = document.getElementById("table3");


    w.style.display = "none";
    y.style.display = "block";
    x.style.display = "none";
    z.style.display = "none";

    
  
}
function maintenance() {
    var w = document.getElementById("table4")
    var y = document.getElementById("table1");
    var x = document.getElementById("table2");
    var z = document.getElementById("table3");

    w.style.display = "none";
    y.style.display = "none";
    x.style.display = "block";
    z.style.display = "none";
  
}
function borrow() {
    var w = document.getElementById("table4")
    var y = document.getElementById("table1");
    var x = document.getElementById("table2");
    var z = document.getElementById("table3");

    w.style.display = "none";
    y.style.display = "none";
    x.style.display = "none";
    z.style.display = "block";
  
}

function inventory() {
    var w = document.getElementById("table4")
    var y = document.getElementById("table1");
    var x = document.getElementById("table2");
    var z = document.getElementById("table3");

    w.style.display = "block";
    y.style.display = "none";
    x.style.display = "none";
    z.style.display = "none";
  
}
