async function controllaCredenziali() {
    const username = documenti.getElementById('username').value;
    const password = documenti.getElementById('password').value;
    if (!username || !password) return alert("scrivi username e password");
    const res = await fetch('/login?username=${(username)} & password =$ {("password")}') ;
    const dati = await res.json();
    document.getElementById('risposta-saluto').innerText = dati.messaggio;
} 