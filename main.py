from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize the application
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    quantity: int


class Input_JSON(BaseModel):
    customer_id: str
    items: List[Item]


@app.post("/sort")
def sort_simple(arr: []):
    arr.sort()
    return {
        "sorted_array": arr
    }


# 1. The Client sends an HTTP request to this URL endpoint
# The {user_input} part extracts info from the URL as a parameter
@app.get("/process/{user_input}")
def process_data(user_input: str):
    # 2. The microservice uses the parameter to inform its execution
    processed_string = user_input.upper()
    character_count = len(user_input)

    # 3. The microservice sends back the output
    # FastAPI automatically converts this Python dictionary into JSON format
    return {
        "original": user_input,
        "processed": processed_string,
        "length": character_count,
        "status": "success"
    }


