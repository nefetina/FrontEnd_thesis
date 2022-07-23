
function validate ()
{
    var un = document.forms["log"]["uname"].value;
    var up = document.forms["log"]["upass"].value;
    
    if(un == "INSTRUCTOR@gmail.com" && up == "instructor")
    {
        window.location.href="HOMEPAGE.html";
    }
    else if(un == "UITCSTAFF@gmail.com" && up == "uitcstaff")
    {
        window.location.href="EQUIPMENT_DEVICE.html";
    }

    else
    {
        alert("PLEASE INPUT THE RIGHT USERNAME AND PASSWORD")
    }

}


function isEmpty(){
   let pass = document.getElementById("upass").value; 
   let name = document.getElementById("uname").value;
   
   
   
   if (name != "" && pass != ""  ){
       document.getElementById("log").removeAttribute("disabled");
       
   }
}
                     
                                