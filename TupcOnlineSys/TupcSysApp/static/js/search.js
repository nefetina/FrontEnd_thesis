//SEARCH FUNCTION FOR USERS
function searchBorrow() {

    let rowCountO = 0;
    let inputO, filterO, tableO, trO, i;
    let tdO0, tdO1, tdO2, tdO3, td04, td05, td06, td07;
    let txtValO0, txtValO1, txtValO2, txtValO3, txtValO4, txtValO5, txtValO6, txtValO7;
    inputO = $('#searchBorrow').val();
    console.log(inputO)
    filterO = inputO.toUpperCase();
    tableO = document.getElementById("idtable3");
    trO = tableO.getElementsByTagName("tr");
    for (i = 0; i < trO.length; i++) {
        tdO0 = trO[i].getElementsByTagName("td")[0];
        tdO1 = trO[i].getElementsByTagName("td")[1];
        tdO2 = trO[i].getElementsByTagName("td")[2];
        tdO3 = trO[i].getElementsByTagName("td")[3];
        tdO4 = trO[i].getElementsByTagName("td")[4];
        tdO5 = trO[i].getElementsByTagName("td")[5];
        tdO6 = trO[i].getElementsByTagName("td")[6];
        tdO7 = trO[i].getElementsByTagName("td")[7];

        if (tdO1 || tdO2 || tdO3 || tdO4 || tdO5 || tdO6 || tdO7) {
            txtValO0 = tdO0.textContent || tdO0.innerText;
            txtValO1 = tdO1.textContent || tdO1.innerText;
            txtValO2 = tdO2.textContent || tdO2.innerText;
            txtValO3 = tdO3.textContent || tdO3.innerText;
            txtValO4 = tdO4.textContent || tdO4.innerText;
            txtValO5 = tdO5.textContent || tdO5.innerText;
            txtValO6 = tdO6.textContent || tdO6.innerText;
            txtValO7 = tdO7.textContent || tdO7.innerText;
            if (txtValO0.toUpperCase().indexOf(filterO) > -1 || txtValO1.toUpperCase().indexOf(filterO) > -1 ||
                txtValO2.toUpperCase().indexOf(filterO) > -1 || txtValO3.toUpperCase().indexOf(filterO) > -1 ||
                txtValO4.toUpperCase().indexOf(filterO) > -1 || txtValO5.toUpperCase().indexOf(filterO) > -1 ||
                txtValO6.toUpperCase().indexOf(filterO) > -1 || txtValO7.toUpperCase().indexOf(filterO) > -1) {
                trO[i].style.display = "";
                rowCountO++;
            } else {
                trO[i].style.display = "none";
            }
        };
    };
    if (rowCountO == 0) {
        $("#no-searchB").css("display", "block");
    } else {
        $("#no-searchB").css("display", "none");
        rowCountO = 0;
    }
};