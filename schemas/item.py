from pydantic import BaseModel

class Item_add(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str


class Item_info(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str