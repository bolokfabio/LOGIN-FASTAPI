from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()
df = pd.read_excel("/workspaces/LOGIN-FASTAPI/dati.xlsx")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse('static/index.html')

@app.post("/login")
def controlla(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "xxx123":
        return {"messaggio": 1}
    else:
        return {"messaggio": 0}

@app.post("/login.Pandas")
def controlla_password(username: str = Form(...), password: str = Form(...)):
    risultato = df[(df["username"] == username)&(df["password"] == password)]
    if not risultato.empty:
        return {"messaggio":1}
    else:
        return {"messaggio":0}