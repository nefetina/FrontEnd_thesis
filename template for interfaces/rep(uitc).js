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


function next() {
    var y = document.getElementById("tableform1");
    var x = document.getElementById("tableform2");
    
    y.style.display = "none";
    x.style.display = "block";
    

    
  
}
function back() {
    var y = document.getElementById("tableform1");
    var x = document.getElementById("tableform2");
    
    y.style.display = "block";
    x.style.display = "none";
    

    
  
}