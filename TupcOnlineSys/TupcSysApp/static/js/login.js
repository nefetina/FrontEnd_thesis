function validate ()
{
    var un = document.forms["log"]["uname"].value;
    var up = document.forms["log"]["upass"].value;
    
    if(un == "faculty" && up == "faculty1")
    {
        window.location.href="{% url 'TupcSysApp:UitcHome'%}";
    }
    else if(un == "uitc" && up == "uitc1")
    {
        window.location.href="{% url 'TupcSysApp:FacultyHome'%}";
    }
    else if(un == "student" && up == "student1")
    {
        window.location.href="{% url 'TupcSysApp:StudentHome'%}";
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
                     
                                