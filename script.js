function crearCorazon() {

    const nombreInput =
    document.getElementById("nombre").value.trim();

    const nombre =
    nombreInput || "AMOR";

    const heart =
    document.getElementById("heart");

    let texto = "";

    let index = 0;

    for(let y = 1.5; y > -1.5; y -= 0.12){

        let linea = "";

        for(let x = -1.5; x < 1.5; x += 0.06){

            let formula =
            Math.pow(x * x + y * y - 1, 3)
            - x * x * y * y * y;

            if(formula <= 0){

                linea +=
                nombre[index % nombre.length];

                index++;

            }else{

                linea += " ";
            }
        }

        texto += linea + "\n";
    }

    heart.textContent = texto;
}

crearCorazon();