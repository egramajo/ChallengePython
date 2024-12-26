from ast import List
from fastapi import APIRouter, Form, Request
from schemas.item import Item_info, Item_add
import services.services as svc


router = APIRouter(prefix="/items",
                   tags=["items"])


@router.get("/detail")
async def hello():
     return {"message": "Aloha"}


@router.post("/add")
async def create_character(item_add: Item_add):
    '''
    Ruta para agregar un nuevo personaje
    '''
    svc.add_character(item_add)
    return item_add


@router.delete("/delete/{id}")
async def delete_character(id = int):
    '''
    Ruta para eliminar un personaje por su id
    '''    
    svc.delete_character_by_id(id)
    return id


@router.get("/getAll")
async def get_all_character():
    '''
    Ruta para buscar todos los personajes guardados en la lista.
    '''
    characters = svc.get_all_characters()
    
    return characters


@router.get("/get/{name}")
async def get_character_by_name(name = str):
    '''
    Ruta para buscar un personaje por su nombre
    '''
    character = svc.get_character_by_name(name)
    
    return character





