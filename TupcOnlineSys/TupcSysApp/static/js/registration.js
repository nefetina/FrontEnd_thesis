const e = require("express");

function next1() {

    var fgsfe = document.getElementById("id_gsfe").value;
    var idnum = document.getElementById("id_username").value;
    const gsfe = document.getElementsByName("gsfes");
    const idno = document.getElementsByName("idnums");

    for (let i = 0; i < idno.length; i++) {
        var id = idno[i].value;
        if (id == idnum){
            var a = "authenticated";
            var row = i;
            break
        }
      }
    for (let x = 0; x < gsfe.length; x++) {
        var gs = gsfe[x].value;
        
        if (gs == fgsfe && id == idnum){
            var b = "authenticated";
            var row1 = x;
            break
        }
    }
    if (a == "authenticated" && b == "authenticated" && row == row1){

        var x = document.getElementById("form1");
        var y = document.getElementById("form2");
        var Z = document.getElementById("form3");
        x.style.display = "none";
        y.style.display = "block";
        Z.style.display = "none";
    }
    else if (fgsfe == "" || idnum == ""){
        alert("Please fill up the form.")
    }
    else {
        alert("Your GSFE Account or ID Number is not in the list, or please recheck all your input.");
    }

    



}

function next2() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var Z = document.getElementById("form3");
    x.style.display = "none";
    y.style.display = "none";
    Z.style.display = "block";

}
function back2() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var Z = document.getElementById("form3");
    x.style.display = "none";
    y.style.display = "block";
    Z.style.display = "none";

}
function back1() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var Z = document.getElementById("form3");
    x.style.display = "block";
    y.style.display = "none";
    Z.style.display = "none";

}

function return1() {
    window.location.href = '/';
}
