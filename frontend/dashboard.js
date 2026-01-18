const BASE_URL = "http://127.0.0.1:8000";

function addPatient() {
    const name = document.getElementById("pname").value;
    const severity = document.getElementById("severity").value;

    fetch(`${BASE_URL}/patients/?name=${name}&severity=${severity}`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => show(data));
}

function addResource() {
    fetch(`${BASE_URL}/resources/?resource_type=ICU_BED`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => show(data));
}

function allocate() {
    fetch(`${BASE_URL}/allocate/`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => show(data));
}

function show(data) {
    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}
