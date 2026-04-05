function addAttendance() {
    const name = document.getElementById("name").value;
    const roll = document.getElementById("roll").value;
    const status = document.getElementById("status").value;

    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, roll, status })
    })
    .then(res => res.json())
    .then(() => {
        alert("Added ✅");
        loadData();
    });
}

function loadData() {
    fetch('/get')
    .then(res => res.json())
    .then(data => {
        const table = document.getElementById("tableBody");
        table.innerHTML = "";

        data.forEach(row => {
            table.innerHTML += `
                <tr>
                    <td>${row.name}</td>
                    <td>${row.roll_no}</td>
                    <td>${row.status}</td>
                    <td>${row.date}</td>
                </tr>
            `;
        });
    });
}

function clearData() {
    fetch('/clear')
    .then(() => {
        alert("Attendance Cleared ✅");
        loadData();
    });
}

window.onload = loadData;