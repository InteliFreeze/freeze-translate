from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

class Text(BaseModel):
    text: str = "";

app = FastAPI()

@app.post("/en-to-pt/")
async def create_item(item: Text):
    translator = Translator()
    translated = translator.translate(item.text, src='en', dest='pt')
    
    return {'text_str': translated.text, 'Status': 'success'}


