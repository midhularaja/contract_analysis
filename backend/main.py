from fastapi import FastAPI, UploadFile, File
from processor import process_contract_logic
import json
import datetime
import os
import uvicorn

app = FastAPI()

@app.post("/analyze")
async def analyze_contract(file: UploadFile = File(...)):
    content = await file.read()
    result = process_contract_logic(content, file.filename)
    
    if not os.path.exists("logs"): os.makedirs("logs")
    with open("logs/audit_log.json", "a") as f:
        log = {"timestamp": str(datetime.datetime.now()), "file": file.filename}
        f.write(json.dumps(log) + "\n")
    return result

# THIS PART MUST BE AT THE VERY BOTTOM
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    