# CS361 Key Generation Service

A microservice that generates Ed25519 key pairs, signs data, and verifies digital signatures via REST API.

## Team
- Kairon Johnson
- Thao Nguyen


## Usage / Testing Instructions
# Key Generation Service (CS361)

FastAPI microservice providing Ed25519 key generation, signing, and verification.

## Setup

1. Create and activate a Python virtual environment:

`
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
`

2. Install dependencies

`
pip install -r requirements.txt
`

## Running the Server

`
fastapi dev main.py
`

## UML Diagram

<img width="462" height="538" alt="image" src="https://github.com/user-attachments/assets/e1e9566b-511d-42c7-b26f-9ae06359aeba" />
