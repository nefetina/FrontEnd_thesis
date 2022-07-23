function openNav(){
   
    var y = document.getElementById("mySidebar");
    var x = document.getElementById("open");
    var z = document.getElementById("close");
   
    y.style.display = "block";
    x.style.display = "block";
    z.style.display = "block";
    

}

function closeNav(){
    
    var y = document.getElementById("mySidebar");
    var x = document.getElementById("close");
    var z = document.getElementById("open");

    y.style.display = "none";
    x.style.display = "none";
    z.style.display = "block";
    
}

