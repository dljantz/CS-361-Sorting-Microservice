from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the application
app = FastAPI()

"""
class Int_Array(BaseModel):
    ints: [int]


@app.post("/sort")
def sort_simple(arr: Int_Array):
    # arr.sort()
    return {
        "unchanged_array": arr
    }
"""


@app.post("/test")
def proof_of_concept():
    return {}
