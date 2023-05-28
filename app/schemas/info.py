
def infoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "info": str(item["info"]),
        "last_update": str(item["last_update"]),
        "author": str(item["author"])
    }

def infosEntity(entity) -> list:
    return [infoEntity(item) for item in entity]