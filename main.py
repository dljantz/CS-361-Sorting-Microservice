from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize the application
app = FastAPI()


class Int_Array(BaseModel):
    ints: List[int]


class Obj(BaseModel):
    rank: int
    info: dict


class Obj_Array(BaseModel):
    objs: List[Obj]


@app.post("/sort_ints")
def sort_simple(arr: Int_Array):
    numbers = arr.ints
    numbers.sort()
    return {
        "sorted_array": numbers
    }


@app.post("/sort_objects")
def sort_objects(arr: Obj_Array):
    objs = arr.objs
    sorted_objs = sorted(objs, key=lambda x: x.rank)
    return {
        "objects": sorted_objs
    }


@app.post("/test")
def proof_of_concept():
    return {}
