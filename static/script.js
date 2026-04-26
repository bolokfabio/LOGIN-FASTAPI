async function loggati() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert("Inserisci username e password");
        return;
    }

    const res = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `username=${username}&password=${password}`
    });

    const dati = await res.json();

    if (dati.messaggio == 1) {
        document.getElementById("risultato").innerText = "Accesso effettuato";
    } else {
        document.getElementById("risultato").innerText = "Accesso negato";
    }
}

document.getElementById('btn_login').addEventListener('click', loggati);