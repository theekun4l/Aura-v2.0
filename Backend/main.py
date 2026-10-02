from fastapi import FastAPI
from pydantic import Field,BaseModel
from Backend.Services.aura import Aura
from fastapi.middleware.cors import CORSMiddleware

#creating Aura class object
aura = Aura()

class AskRequest(BaseModel):
    prompt: str
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask_aura")
def Ask(request : AskRequest ):
    result = aura.command(request.prompt)

    return result