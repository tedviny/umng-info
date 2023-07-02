import logging
from app.models.umng_info import Info
from app.config.db import conn
from app.schemas.info import infoEntity, infosEntity
from bson import ObjectId

logging.basicConfig(level=logging.DEBUG)

def umng_general_info():
    print(conn.local.infos.find())
    print(infosEntity(conn.local.infos.find()))
    return infosEntity(conn.local.infos.find())

def add_info(info: Info):
    conn.local.infos.insert_one(dict(info))

def update_info(id:str, info: Info):
    conn.local.infos.find_one_and_update(
        {"_id":ObjectId(id)},
        {"$set":dict(info)})

def delete_info(id:str):
    try:
        conn.local.infos.find_one_and_delete(
    {"_id":ObjectId(id)})
    except:
        logging.info("Information not found")

