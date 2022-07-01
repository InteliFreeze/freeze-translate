from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware

class Text(BaseModel):
    text: str = "";

app = FastAPI()

origins = [
    "https://ifreeze.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/en-to-pt/")
async def create_item(item: Text):
    translator = Translator()
    translated = translator.translate(item.text, src='en', dest='pt')
    
    return {'text_str': translated.text, 'Status': 'success'}


