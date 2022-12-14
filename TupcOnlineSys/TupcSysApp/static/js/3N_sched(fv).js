
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


function lab1(){
    var x = document.getElementById("idtable");
    var y = document.getElementById("idtable1");
    var z = document.getElementById("idtable2");
    
    x.style.display = "block";
    y.style.display = "none";
    z.style.display = "none";

  
}

function lab2(){
    var x = document.getElementById("idtable");
    var y = document.getElementById("idtable1");
    var z = document.getElementById("idtable2");
    
    x.style.display = "none";
    y.style.display = "block";
    z.style.display = "none";

  
}
function lab3(){
    var x = document.getElementById("idtable");
    var y = document.getElementById("idtable1");
    var z = document.getElementById("idtable2");
    
    x.style.display = "none";
    y.style.display = "none";
    z.style.display = "block";

  
}