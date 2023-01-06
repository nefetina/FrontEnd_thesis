
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


function requestforlab() {
    var a = document.getElementById("table1");
    var b = document.getElementById("table2");
    

    a.style.display = "block";
    b.style.display = "none";
  
}


function labsched() {
    var a = document.getElementById("table1");
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