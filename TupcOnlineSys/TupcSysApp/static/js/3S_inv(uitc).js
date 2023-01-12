
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

function myFunction() {


var table = document.getElementById("mytable1");
var tr = table.getElementsByTagName("tr");
for (i = 0; i < tr.length; i++) {
  var td = tr[i].getElementsByTagName("td")[4];


  if (td) {
    txtValue = td.textContent || td.innerText;
    if (txtValue == "Available") {
        var buttonr = document.getElementsByName("return")[i - 1];
        buttonr.disabled = false;   

    }
    if (txtValue == "Not working") {
        var buttonr = document.getElementsByName("return")[i - 1];
        buttonr.disabled = false;
        
}
    if (txtValue == "Replaced" || txtValue == "Defect") {
        var buttonr = document.getElementsByName("return")[i - 1];
        buttonr.disabled = true;
        tr[i].hidden = true;

    }
  } 

}
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
}