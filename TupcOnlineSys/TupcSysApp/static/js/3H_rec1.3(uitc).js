
window.onload = function() {

    var span_Text = document.getElementById("id_notif").innerText;
    if (span_Text == 0){
        document.getElementById("id_notif").hidden = true;
    }
    else if (span_Text > 0){
        document.getElementById("id_notif").hidden = false;
    }

    var span_Text1 = document.getElementById("net_notif").innerText;
    if (span_Text1 == 0){
        document.getElementById("net_notif").hidden = true;
    }
    else if (span_Text1 > 0){
        document.getElementById("net_notif").hidden = false;
    }

    var span_Text2 = document.getElementById("sched_notif").innerText;
    if (span_Text2 == 0){
        document.getElementById("sched_notif").hidden = true;
    }
    else if (span_Text2 > 0){
        document.getElementById("sched_notif").hidden = false;
    }

    var span_Text3 = document.getElementById("report_notif").innerText;
    if (span_Text3 == 0){
        document.getElementById("report_notif").hidden = true;
    }
    else if (span_Text3 > 0){
        document.getElementById("report_notif").hidden = false;
    }
  };
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