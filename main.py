
from fastapi import FastAPI, File, UploadFile
from ocr_test import extract_meter_info

app = FastAPI()

@app.post("/extract-info/")
async def extract_info(file: UploadFile = File(...)):
    contents = await file.read()
    info = extract_meter_info(contents)
    return {"filename": file.filename, "extracted_info": info}
