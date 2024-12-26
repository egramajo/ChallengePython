import json
import os
from starlette import status
from fastapi import HTTPException
from schemas.item import Item_add


file_name = 'data.json'


#funcion para traer a todos los personajes
def get_all_characters():
    with open(file_name, 'r') as f:
        dataJSON = json.load(f)
    return dataJSON


#funcion para buscar un personaje por su nombre.
def get_character_by_name(name):
    with open(file_name, 'r') as f:
        dataJSON = json.load(f)
        
    search_result = [item for item in dataJSON if item["name"]==name]
    return search_result


#funcion para agregar un personaje a la lista.
def add_character(item_add):
    new_item = dict(item_add)
    
    with open(file_name, 'r') as f:
        dataJSON = json.load(f)
    
    if (item_exist_in_list(new_item, dataJSON)):
        dataJSON.append(new_item)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="El personaje ya existe")
    os.remove(file_name)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dataJSON, indent=2))
    return True
        

#funcion para eliminar un personaje de la lista.
def delete_character_by_id(id):
    with open(file_name, 'r') as f:
        dataJSON = json.load(f)
        
    for idx, data in enumerate(dataJSON):
        if data['id'] == int(id):
            dataJSON.pop(idx)
          
    os.remove(file_name)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dataJSON, indent=2))
    return id
        
    
#funcion
def item_exist_in_list(new_item, item_list):
    for item in item_list:
        if item['id'] == new_item['id']:
            return False
        
    return True
        
    
    
    