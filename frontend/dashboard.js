function allocate() {
  fetch("http://127.0.0.1:8000/allocate/", {
    method: "POST"
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText = JSON.stringify(data, null, 2);
  });
}
