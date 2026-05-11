function crearCorazon() {
  const nombre = document.getElementById("nombre").value.trim();

  if (nombre === "") {
    alert("Escribe un nombre primero");
    return;
  }

  let resultado = "";

  for (let y = 1.5; y > -1.5; y -= 0.12) {
    for (let x = -1.5; x < 1.5; x += 0.06) {
      let formula = Math.pow(x * x + y * y - 1, 3) - x * x * y * y * y;

      if (formula <= 0) {
        resultado += nombre;
      } else {
        resultado += " ";
      }
    }
    resultado += "\n";
  }

  document.getElementById("corazon").textContent = resultado;
}