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

function isNumberKey(evt)
{
  var charCode = (evt.which) ? evt.which : event.keyCode;
    if (charCode == 45) {
        return true;
    }
    if ((charCode > 47 && charCode <58))
    {
        return true;
    }
  return false;
}

