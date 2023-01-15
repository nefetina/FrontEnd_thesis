
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
    var table = document.getElementById("myTable");
    var tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName("td")[7];
    var td1 = tr[i].getElementsByTagName("td")[1];
    var td2 = tr[1].getElementsByTagName("td")[1];


    if (td, td1) {
        txtValue = td.textContent || td.innerText;
        txtValue1 = td1.textContent || td1.innerText;

        if (txtValue == "Borrowed" && td2 != "[object HTMLTableCellElement]" && txtValue1 == "Student" && tr.length==3) {
 
            document.getElementsByName("btnreject")[i-2].hidden = true;
            document.getElementsByName("btnapproved")[i-2].hidden = true;
            document.getElementsByName("btnnotify")[i-2].hidden = false;
            document.getElementsByName("btnreturn")[i-2].hidden = false;
            
            

        }
        else if (txtValue == "Borrowed") {

            document.getElementsByName("btnreject")[i-1].hidden = true;
            document.getElementsByName("btnapproved")[i-1].hidden = true;
            document.getElementsByName("btnnotify")[i-1].hidden = false;
            document.getElementsByName("btnreturn")[i-1].hidden = false;
            
            

        }
        
        else if (txtValue == "On Process") {
            document.getElementsByName("btnreject")[i-1].hidden = false;
            document.getElementsByName("btnapproved")[i-1].hidden = false;
            document.getElementsByName("btnnotify")[i-1].hidden = true;
            document.getElementsByName("btnreturn")[i-1].hidden = true;
            
    }
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

function mspp() {

    for (let i = 0; i < document.getElementsByName('remarks').length; i++) {
        selectElement = document.getElementsByName('remarks')[i];
        output = selectElement.options[selectElement.selectedIndex].value;
        
    
            
            if (output == "Missing some parts"){
                const z = document.getElementsByName("msp");
                z[i].hidden = false;
                

                
            }
            if (output != "Missing some parts"){
                const z = document.getElementsByName("msp");
                z[i].hidden = true;
                
        }
        
        
    }
    }
    
    


function mspp1() {

    for (let i = 0; i < document.getElementsByName('remarks1').length; i++) {
        selectElement = document.getElementsByName('remarks1')[i];
        output = selectElement.options[selectElement.selectedIndex].value;
        
    
            
            if (output == "Missing some parts"){
                const z = document.getElementsByName("msp1");
                z[i].hidden = false;
                

                
            }
            if (output != "Missing some parts"){
                const z = document.getElementsByName("msp1");
                z[i].hidden = true;
                
        }
        
        
    }
    }

function returned1() {
    for (let i = 0; i < document.getElementsByName('remarks').length; i++) {
        selectElement = document.getElementsByName('remarks')[i];
        for (let i = 0; i < selectElement.length; i++) {
            const z = document.getElementsByName("msp1");
            z[i].hidden = true;
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






