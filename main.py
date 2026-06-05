from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

# Initialize the application
app = FastAPI()


class Int_Array(BaseModel):
    ints: List[int]


# Updated to accept a list of any dictionaries
class Flexible_Obj_Array(BaseModel):
    objs: List[Dict[str, Any]]


@app.post("/sort_ints")
def sort_simple(arr: Int_Array):
    numbers = arr.ints
    numbers.sort()
    return {
        "sorted_array": numbers
    }


@app.post("/sort_objects")
def sort_objects(arr: Flexible_Obj_Array, sort_key: str = "rank"):
    objs = arr.objs

    # Ensure the requested sort_key exists in all objects to avoid a KeyError (500 Server Error)
    if not all(sort_key in obj for obj in objs):
        raise HTTPException(
            status_code=400,
            detail=f"Cannot sort. The key '{sort_key}' is missing from one or more objects."
        )

    # Sort dynamically by the requested key
    sorted_objs = sorted(objs, key=lambda x: x[sort_key])

    return {
        "objects": sorted_objs
    }


@app.post("/test")
def proof_of_concept():
    return {}