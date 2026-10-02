from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Aura V2 is running 🚀"}