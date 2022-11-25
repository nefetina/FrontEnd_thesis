function next1() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    x.style.display = "none";
    y.style.display = "block";
   

}



function back1() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    x.style.display = "block";
    y.style.display = "none";
  

}

function return1() {
    window.location.href = '/';
}