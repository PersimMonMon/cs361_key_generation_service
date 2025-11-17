from app.models import GenerateRequest, GenerateResponse
from app.crypto import generate_ed25519_keypair

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.post("/generateKeyPair", response_model=GenerateResponse, tags=["keys"])
def generate_keypair(req: GenerateRequest):
    if req.algorithm.lower() != "ed25519":
        raise HTTPException(status_code=400, detail="Only Ed25519 is supported in this service.")
    public_b64, private_b64 = generate_ed25519_keypair()
    return GenerateResponse(public_key=public_b64, private_key=private_b64)