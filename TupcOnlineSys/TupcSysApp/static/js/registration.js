function next1() {
    var x = document.getElementById("form1");
    var y = document.getElementById("form2");
    var Z = document.getElementById("form3");
    x.style.display = "none";
    y.style.display = "block";
    Z.style.display = "none";

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