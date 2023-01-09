window.onload = function() {
    

    var status = document.getElementById("status");
    var y = document.getElementById("repairmaintenanceform");
    var x = document.getElementById("queue");
    var z = document.getElementById("tableform3");
    if (status == null){
        y.hidden = false;
        x.hidden = true;
        z.hidden = true;
    }
    else if (status != null) {
        if (status.innerText == "Approved"){
            y.hidden = true;
            x.hidden = true;
            z.hidden = false;
        }
        else if (status.innerText == "Notified" || status.innerText == "On Process"){
            y.hidden = true;
            x.hidden = false;
            z.hidden = true;
        }
    

    }




}
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
/*breadcrumb buttons navigation*/ ///////////////
function requestforrep() {

    var y = document.getElementById("form1");
    var x = document.getElementById("form2");
    var z = document.getElementById("form3");

    y.style.display = "block";
    x.style.display = "none";
    z.style.display = "none";
    var request = document.getElementById("request").innerText;


}
function requestforpassreset() {

    var y = document.getElementById("form1");
    var x = document.getElementById("form2");
    var z = document.getElementById("form3");

    y.style.display = "none";
    x.style.display = "block";
    z.style.display = "none";

}

function borrow() {
    var y = document.getElementById("form1");
    var x = document.getElementById("form2");
    var z = document.getElementById("form3");

    y.style.display = "none";
    x.style.display = "none";
    z.style.display = "block";

}


function other() {
    var a = document.getElementById("others");
    var b = document.getElementById("other_input");

    if (a.checked == true) {
        b.disabled = false;
        a.value = b.value();
    }
    else if(a.checked == false) {
        b.disabled = true;

}
}
 