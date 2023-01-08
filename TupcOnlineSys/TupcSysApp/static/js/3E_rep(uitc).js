
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
    const fbstat = document.getElementsByName("fbstat");
    
    for (let i = 0; i < fbstat.length; i++) {
        var stat = fbstat[i].innerText;
        if (stat == "Borrowed"){
            document.getElementsByName("btnreject")[i].hidden = true;
            document.getElementsByName("btnapproved")[i].hidden = true;
            document.getElementsByName("btnnotify")[i].hidden = false;
            document.getElementsByName("btnreturn")[i].hidden = false;
        }
        
      }
  };
  var x2 = document.getElementById("table1");
  var z2 = document.getElementById("table2");
  var y2 = document.getElementById("table3");
  var v2 = document.getElementById("table4");
  x2.hidden = false;
  z2.hidden = true;
  y2.hidden = true;
  v2.hidden = true;



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




/*tableform 1.1-1.3 navigation*/ ///////////////

function next1() {

    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = true;
    document.getElementById("tableform2").hidden = false;

    x1.hidden = true;
    h.hidden = true;




}


function next2() {
    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = true;
    document.getElementById("tableform2").hidden = true;

    x1.hidden = true;
    h.hidden = true;




}

function back1() {
    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = false;
    document.getElementById("tableform2").hidden = true;

    x1.hidden = true;
    h.hidden = true;



}

function back2() {
    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = false;
    document.getElementById("tableform2").hidden = true;

    x1.hidden = true;
    h.hidden = true;



}


/*tableform 2.1-2.3 navigation*/ ///////////////

function next3() {
    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = false;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = false;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;



}


function next4() {
    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = false;


    w2.hidden = false;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;




}

function back3() {
    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = false;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = false;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;



}

function back4() {
    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = false;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = false;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;



}


/*opening the form from tables*/ ///////////////
function form111() {


    var y1 = document.getElementById("tableform1");
    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = false;
    document.getElementById("tableform2").hidden = true;

    x1.hidden = true;
    h.hidden = true;

}
function return222() {
    var y1 = document.getElementById("tableform1");
    var x1 = document.getElementById("searchform");
    var h = document.getElementById("tablerp");
    document.getElementById("tableform1").hidden = true;
    document.getElementById("tableform2").hidden = true;

    x1.hidden = false;
    h.hidden = false;
}



function requestforrep() {

    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");
    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;
    w2.hidden = true;
    x2.hidden = false;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;




}




function requesforpassres() {

    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");
    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;
    w2.hidden = true;
    x2.hidden = true;
    z2.hidden = false;
    y2.hidden = true;
    v2.hidden = true;


}


function maintenanceform() {

    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = false;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = false;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = true;


}

function maintenance() {

    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = true;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = false;
    v2.hidden = true;

}


function borrow() {
    

    var x2 = document.getElementById("table1");
    var z2 = document.getElementById("table2");
    var y2 = document.getElementById("table3");
    var v2 = document.getElementById("table4");
    var w2 = document.getElementById("myformm ");

    document.getElementById("tableform4").hidden = true;
    document.getElementById("tableform5").hidden = true;
    document.getElementById("tableform6").hidden = true;


    w2.hidden = true;
    x2.hidden = true;
    z2.hidden = true;
    y2.hidden = true;
    v2.hidden = false;

}


/*breadcrumb buttons navigation*/ ///////////////






function approved(){
    document.getElementById("btnreject").hidden = true;
    document.getElementById("btnapproved").hidden = true;
    document.getElementById("btnnotify").hidden = false;
    document.getElementById("btnreturn").hidden = false;
}


function returned(){
    document.getElementById("btnreject").hidden = false;
    document.getElementById("btnapproved").hidden = false;
    document.getElementById("btnnotify").hidden = true;
    document.getElementById("btnreturn").hidden = true;
}