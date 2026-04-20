from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Spieghiamo a FastAPI che i file dentro "static" sono accessibili
app.mount("/static", StaticFiles(directory="static"), name="static") # mount = montare , dice che da adesso i StaticFiles sono accessibili e gli dice che cosa può usare


@app.get("/") # endpoint  punto dove richimiamo il nostro server web, lo / significa che volgio la pagna HTML
def home():
    # Restituisce direttamente il file HTML
    return FileResponse('static/index.html')
