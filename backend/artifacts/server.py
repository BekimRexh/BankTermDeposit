from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import utils
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/marital_status')
async def marital_status():
    marital = utils.get_marital_status()
    return {'marital_status': marital}



