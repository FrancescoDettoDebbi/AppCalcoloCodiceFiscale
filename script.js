let comuni = [];

let testo = document.getElementById("input-field");

async function getComuni(stringa){
    let data = await fetch("http://127.0.0.1:8000/comuni/"+stringa);
    let dataJ = await data.json();
    comuni = dataJ.comuni;
}

function createOption() {
    let stringa = testo.value;
    let ul = document.getElementById("comuni");
    ul.innerHTML = "";
    if (stringa == ""){return}

    getComuni(stringa);
    for (let i = 0; i < comuni.length; i ++){
        if(comuni[i].toUpperCase().includes(stringa.toUpperCase())){
            let item = document.createElement("li");
            item.textContent = comuni[i];
            ul.appendChild(item);
            item.addEventListener("click", () => {testo.value = item.textContent; ul.innerHTML = ""})
        }
    }
}

async function calcola(){
    let nome = document.getElementById("first-name-field").value;
    let cognome = document.getElementById("last-name-field").value;
    let dataNasc = document.getElementById("data-nascita").value;
    let sesso = document.getElementById("sesso").value;
    let comune = testo.value;
    let data = await fetch("http://127.0.0.1:8000/codice?name=" + nome + "&last_name=" + cognome +
    "&date=" + dataNasc + "&sex=" + sesso + "&city=" + comune);
    let dataJ = await data.json();
    document.getElementById("cod-fiscale").textContent = dataJ.codiceFiscale;
}

createOption();
testo.addEventListener("input",() => {createOption();});
