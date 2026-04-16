from fastapi import FastAPI
from pydantic import BaseModel
from utils import calculate_similarity
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    codes: list[str]

@app.get("/")
def home():
    return {"message": "Code Plagiarism Checker API Running"}

@app.post("/check")
def check_code(data: CodeInput):
    similarity = calculate_similarity(data.codes)
    return {"similarity_matrix": similarity}