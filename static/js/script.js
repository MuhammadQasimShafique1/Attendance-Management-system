// ================================
// Student Search
// ================================

function searchStudent() {

    let input = document.getElementById("searchInput");

    if (!input) return;

    let filter = input.value.toUpperCase();

    let table = document.getElementById("studentTable");

    if (!table) return;

    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let td = tr[i].getElementsByTagName("td")[1];

        if (td) {

            let txtValue = td.textContent || td.innerText;

            tr[i].style.display = txtValue.toUpperCase().indexOf(filter) > -1
                ? ""
                : "none";

        }

    }

}

// ================================
// Report Search
// ================================

function searchReport() {

    let input = document.getElementById("reportSearch");

    if (!input) return;

    let filter = input.value.toUpperCase();

    let table = document.getElementById("reportTable");

    if (!table) return;

    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let td = tr[i].getElementsByTagName("td")[1];

        if (td) {

            let txtValue = td.textContent || td.innerText;

            tr[i].style.display = txtValue.toUpperCase().indexOf(filter) > -1
                ? ""
                : "none";

        }

    }

}

// ================================
// Delete Confirmation
// ================================

function confirmDelete(name){

    return confirm(

        "Are you sure you want to delete " +

        name +

        " ?"

    );

}

// ================================
// Auto Hide Alerts
// ================================

window.onload = function(){

    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        setTimeout(function(){

            alert.style.display = "none";

        },3000);

    });

};

// ================================
// Welcome Message
// ================================

console.log("Student Attendance System Loaded Successfully");