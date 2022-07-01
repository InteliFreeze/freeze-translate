from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

class Text(BaseModel):
    text: str = None;

app = FastAPI()

@app.post("/en-to-pt/")
async def create_item(item: Text):
    translator = Translator()
    text = translator.translate(item.text, src='en', dest='pt')
    return {'text_str': text, 'Status': 'success'}


