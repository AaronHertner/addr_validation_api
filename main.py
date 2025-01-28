from fastapi import FastAPI
from model import AddressValidator

import json

# Initialize the FastAPI app
app = FastAPI()
client = AddressValidator()

# Define root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Address Validation API!"}

# Define post endpoint
@app.post("/validate-address")
def validate_address(business: str, address: str, sugg_address: str):
    res = client.query(business=business, address=address, sugg_address=sugg_address)
    return {"message": res}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)