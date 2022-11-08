from fastapi import FastAPI
from pydantic import BaseModel
from modules.inference import infer_t5

app = FastAPI()

class Input(BaseModel):
    language: str
    text: str

@app.head("/ping")

@app.post("/invocations")
def invoke(input: Input):
    input_dict = input.dict()
    print(input_dict["language"])
    text = input_dict["language"] + " : " + input_dict["text"]
    # Translate text
    output = infer_t5(text)
    print(' translated_text : ', output)
    return output

@app.get("/ping")
def ping():
    return 'ping'


