from fastapi import APIRouter
from views.umng_info import umng_general_info, add_info, update_info, delete_info
from models.umng_info import Info

router = APIRouter(prefix="/api/v1/infos",)

@router.get("/", tags=["General informations"])
def get_infos():
    return umng_general_info()

@router.post("/", tags=["Add information"])
def add_infos(info: Info):
    add_info(info)
    return "Information added"

@router.put("/{id}", tags=["Update information"])
def update_infos(id: str, info: Info):
    update_info(id,info)
    return "Information is updated"

@router.delete("/{id}", tags=["Update information"])
def delete_infos(id: str):
    delete_info(id)
    return "Information successfully deleted"